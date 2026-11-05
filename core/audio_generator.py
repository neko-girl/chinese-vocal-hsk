"""MiniMax Text-to-Speech (T2A v2) Audio Generator for Chinese Vocal HSK.

Features:
  - Smart File Integrity Checker: skips valid existing files, cleans corrupted stubs.
  - Persistent Cross-Word Text Hash Cache: reuses identical text audio across words (0 API points).
  - Atomic File Writing: prevents partial/corrupted files if interrupted.
  - Audit/Check Mode: deep verification of chapter audio progress and point estimates.
  - Support for 4 MiniMax voice personas (defaults to Option 1: Mature Woman + Office Man).
"""

import os
import sys
import re
import json
import time
import shutil
import urllib.request
import urllib.error
from typing import Dict, List, Optional, Tuple, Any

from .toon_parser import parse_chapter, parse_toon_file
from .compiler import compile_chapter

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# ---------------------------------------------------------------------------
# Lightweight .env Loader (Zero external dependencies)
# ---------------------------------------------------------------------------
def load_env_file(env_path: Optional[str] = None):
    """Loads key-value pairs from .env into os.environ if not already present."""
    if env_path is None:
        env_path = os.path.join(BASE_DIR, '.env')
    if not os.path.isfile(env_path):
        return

    try:
        with open(env_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                if '=' in line:
                    key, val = line.split('=', 1)
                    key = key.strip()
                    val = val.strip().strip("'\"")
                    if key and key not in os.environ:
                        os.environ[key] = val
    except Exception as e:
        print(f"[WARN] Could not parse .env file: {e}")

# Load .env at import time
load_env_file()

# ---------------------------------------------------------------------------
# Voice Configuration
# ---------------------------------------------------------------------------
VOICE_CONFIGS = {
    "mature_woman": {
        "id_key": "MINIMAX_VOICE_MATURE_WOMAN",
        "default_id": "female-chengshu",
        "display_name": "Mature Woman (成熟女性)",
        "tone": "Warm, mature, steady feminine tone"
    },
    "soothing_host": {
        "id_key": "MINIMAX_VOICE_SOOTHING_HOST",
        "default_id": "presenter_female",
        "display_name": "Soothing Host (温润女主播)",
        "tone": "Clear, broadcast-quality presenter delivery"
    },
    "office_man": {
        "id_key": "MINIMAX_VOICE_OFFICE_MAN",
        "default_id": "male-qn-jingying",
        "display_name": "Office Man (职场男音)",
        "tone": "Professional, grounded workplace male cadence"
    },
    "tender_ceo": {
        "id_key": "MINIMAX_VOICE_TENDER_CEO",
        "default_id": "male-qn-badao",
        "display_name": "Tender CEO (霸道/温润总裁)",
        "tone": "Deep, magnetic, resonant executive tone"
    }
}

def get_voice_id(voice_key: str) -> str:
    """Returns the configured MiniMax voice_id for a voice key."""
    cfg = VOICE_CONFIGS.get(voice_key)
    if not cfg:
        return voice_key
    return os.getenv(cfg["id_key"], cfg["default_id"])

# ---------------------------------------------------------------------------
# Strategy 1: File Integrity Checker
# ---------------------------------------------------------------------------
def is_valid_audio_file(filepath: str) -> bool:
    """Checks if a file exists, is non-empty (>128 bytes), and has a valid audio signature.
    
    Protects against 0-byte files, truncated downloads, or API error JSON saved as .mp3.
    """
    if not os.path.isfile(filepath):
        return False
    try:
        size = os.path.getsize(filepath)
        if size < 128:
            return False

        with open(filepath, 'rb') as f:
            header = f.read(4)

        # Check for ID3v2 container header
        if header.startswith(b'ID3'):
            return True

        # Check for MPEG audio frame sync bits (11 set bits: 0xFF followed by 0xE0 mask)
        if len(header) >= 2 and header[0] == 0xFF and (header[1] & 0xE0) == 0xE0:
            return True

        # Fallback for RIFF / WAV headers if any
        if header.startswith(b'RIFF'):
            return True

        return False
    except Exception:
        return False

# ---------------------------------------------------------------------------
# Strategy 2: Persistent Cross-Word Text Hash Cache
# ---------------------------------------------------------------------------
def get_cache_path(chapter_dir: str) -> str:
    return os.path.join(chapter_dir, 'audio', '.cache.json')

def load_audio_cache(chapter_dir: str) -> Dict[str, str]:
    """Loads persistent map of text+voice -> valid relative mp3 file."""
    cache_file = get_cache_path(chapter_dir)
    if not os.path.isfile(cache_file):
        return {}
    try:
        with open(cache_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        valid_cache = {}
        for k, rel_path in data.items():
            full_path = os.path.join(chapter_dir, 'audio', rel_path)
            if is_valid_audio_file(full_path):
                valid_cache[k] = rel_path
        return valid_cache
    except Exception:
        return {}

def save_audio_cache(chapter_dir: str, cache: Dict[str, str]):
    """Atomically writes cache to disk."""
    cache_file = get_cache_path(chapter_dir)
    try:
        os.makedirs(os.path.dirname(cache_file), exist_ok=True)
        tmp = cache_file + '.tmp'
        with open(tmp, 'w', encoding='utf-8') as f:
            json.dump(cache, f, ensure_ascii=False, indent=2)
        os.replace(tmp, cache_file)
    except Exception as e:
        print(f"[WARN] Failed to save audio cache: {e}")

# ---------------------------------------------------------------------------
# MiniMax API Client
# ---------------------------------------------------------------------------
class MiniMaxAudioClient:
    """Synchronous client for MiniMax T2A v2 speech synthesis endpoint."""

    def __init__(self, api_key: Optional[str] = None, api_base: Optional[str] = None, model: Optional[str] = None):
        self.api_key = api_key or os.getenv("MINIMAX_API_KEY", "").strip()
        self.api_base = (api_base or os.getenv("MINIMAX_API_BASE", "https://api.minimax.io/v1")).rstrip('/')
        self.model = model or os.getenv("MINIMAX_MODEL", "speech-02-hd").strip()
        self.group_id = os.getenv("MINIMAX_GROUP_ID", "").strip()

    def is_configured(self) -> bool:
        return bool(self.api_key)

    def synthesize(self, text: str, voice_id: str, speed: float = 1.0) -> bytes:
        """Synthesizes text to MP3 bytes via MiniMax T2A v2 API."""
        if not self.is_configured():
            raise ValueError(
                "MINIMAX_API_KEY is not set. Please add it to your .env file or environment.\n"
                "Example: MINIMAX_API_KEY=your_key_here"
            )

        endpoint = f"{self.api_base}/t2a_v2"
        if self.group_id:
            endpoint += f"?GroupId={self.group_id}"

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        clean_text = text.strip()
        if not clean_text:
            raise ValueError("Cannot synthesize empty text.")

        payload = {
            "model": self.model,
            "text": clean_text,
            "stream": False,
            "voice_setting": {
                "voice_id": voice_id,
                "speed": float(speed),
                "vol": 1.0,
                "pitch": 0
            },
            "audio_setting": {
                "sample_rate": 32000,
                "bitrate": 128000,
                "format": "mp3",
                "channel": 1
            }
        }

        data_bytes = json.dumps(payload).encode('utf-8')
        req = urllib.request.Request(endpoint, data=data_bytes, headers=headers, method="POST")

        try:
            with urllib.request.urlopen(req, timeout=45) as resp:
                resp_data = resp.read()
                resp_json = json.loads(resp_data.decode('utf-8'))
        except urllib.error.HTTPError as e:
            err_body = e.read().decode('utf-8', errors='replace')
            raise RuntimeError(f"MiniMax API HTTP Error {e.code}: {err_body}")
        except Exception as e:
            raise RuntimeError(f"Network error calling MiniMax API: {e}")

        base_resp = resp_json.get("base_resp", {})
        status_code = base_resp.get("status_code", 0)
        status_msg = base_resp.get("status_msg", "")
        if status_code != 0:
            raise RuntimeError(f"MiniMax synthesis failed [Code {status_code}]: {status_msg}")

        audio_hex = resp_json.get("data", {}).get("audio", "")
        if not audio_hex:
            raise RuntimeError(f"MiniMax returned no audio data: {resp_json}")

        return bytes.fromhex(audio_hex)

# ---------------------------------------------------------------------------
# Word Item Extractor
# ---------------------------------------------------------------------------
def extract_chinese_items(word_data: dict) -> List[Tuple[str, str, str]]:
    """Extracts all Chinese text items that require audio from a word dictionary."""
    items: List[Tuple[str, str, str]] = []

    # 1. Headword
    hw = word_data.get('hanzi', '').strip()
    if hw:
        items.append(('headword', 'headword', hw))

    # 2. Example Sentences (1 & 2)
    sentences = word_data.get('example_sentences', [])
    for idx, s in enumerate(sentences, 1):
        txt = s.get('hanzi', '').strip()
        if txt:
            items.append(('sentence', f'sentence_{idx}', txt))

    # 3. Collocations (1..6)
    collocs = word_data.get('collocations', [])
    for idx, c in enumerate(collocs, 1):
        txt = c.get('hanzi', '').strip()
        if txt:
            items.append(('collocation', f'collocation_{idx}', txt))

    # 4. Idioms (1..4)
    idioms = word_data.get('idioms', [])
    for idx, im in enumerate(idioms, 1):
        txt = im.get('hanzi', '').strip()
        if txt:
            items.append(('idiom', f'idiom_{idx}', txt))

    # 5. Extended Reading Passages (1 & 2)
    passages = word_data.get('extended_reading_passages', [])
    for idx, p in enumerate(passages, 1):
        txt = p.get('hanzi', '').strip()
        if txt:
            items.append(('passage', f'passage_{idx}', txt))

    # 6. Character Decomposition (unique characters in headword)
    decomp = word_data.get('character_decomposition', [])
    for ch in decomp:
        char = ch.get('character', '').strip()
        if char:
            items.append(('char', f'char_{char}', char))

    # 7. Look-Alikes
    look_alikes = word_data.get('traps_and_cognates', {}).get('look_alikes', [])
    for la in look_alikes:
        char = la.get('character', '').strip()
        if char:
            items.append(('lookalike', f'lookalike_{char}', char))

    # 8. Etymological Cognates
    cognates = word_data.get('traps_and_cognates', {}).get('etymological_cognates', [])
    for cg in cognates:
        char = cg.get('character', '').strip()
        if char:
            items.append(('cognate', f'cognate_{char}', char))

    return items

# ---------------------------------------------------------------------------
# Strategy 3: Chapter Checker / Audit Mode
# ---------------------------------------------------------------------------
def check_chapter_audio(
    chapter_dir: str,
    voices: Optional[List[str]] = None,
    skip_passages: bool = True,
    item_types: Optional[List[str]] = None
) -> dict:
    """Performs a comprehensive integrity check and status audit of a chapter's audio files.
    
    Verifies every audio file, detects corrupt/0-byte files, and calculates remaining points.
    """
    if voices is None:
        env_voices = os.getenv("MINIMAX_VOICES")
        if env_voices:
            voices = list(VOICE_CONFIGS.keys()) if env_voices.lower() == 'all' else [v.strip() for v in env_voices.split(",") if v.strip()]
        else:
            voices = ["mature_woman", "office_man"]

    words = parse_chapter(chapter_dir)
    audio_base_dir = os.path.join(chapter_dir, 'audio')
    chapter_basename = os.path.basename(chapter_dir)

    total_required = 0
    valid_count = 0
    missing_count = 0
    corrupt_count = 0
    chars_to_synthesize = 0
    already_spent_chars = 0

    seen_texts: Dict[str, str] = {}
    dedup_savings_chars = 0

    print(f"\n==================================================")
    print(f"🔍 Audio Checker & Audit for {chapter_basename}")
    print(f"Total Words        : {len(words)}")
    print(f"Voices Monitored   : {', '.join([VOICE_CONFIGS[v]['display_name'] for v in voices])}")
    print(f"Skip Passages      : {skip_passages}")
    print(f"==================================================")

    for w_idx, w in enumerate(words, 1):
        w_id = int(w.get('id', w_idx))
        hanzi = w.get('hanzi', '')
        word_slug = f"{w_id:02d}_{hanzi}"
        word_audio_dir = os.path.join(audio_base_dir, word_slug)

        items = extract_chinese_items(w)
        if skip_passages:
            items = [item for item in items if item[0] != 'passage']
        if item_types:
            items = [item for item in items if item[0] in item_types]

        for it_type, slug, text in items:
            for v_key in voices:
                total_required += 1
                out_filename = f"{slug}_{v_key}.mp3"
                out_path = os.path.join(word_audio_dir, out_filename)

                if os.path.exists(out_path):
                    if is_valid_audio_file(out_path):
                        valid_count += 1
                        already_spent_chars += len(text)
                        # Register in seen texts for dedup tracking
                        cache_key = f"{text}___{v_key}"
                        if cache_key not in seen_texts:
                            seen_texts[cache_key] = out_path
                    else:
                        corrupt_count += 1
                        print(f"  [CORRUPT FILE DETECTED]: {word_slug}/{out_filename} (Size: {os.path.getsize(out_path)} bytes)")
                        # Remove corrupt file so it can regenerate cleanly
                        try:
                            os.remove(out_path)
                            print(f"    --> Removed corrupted file.")
                        except Exception:
                            pass
                        missing_count += 1
                        chars_to_synthesize += len(text)
                else:
                    missing_count += 1
                    cache_key = f"{text}___{v_key}"
                    if cache_key in seen_texts:
                        dedup_savings_chars += len(text)
                    else:
                        chars_to_synthesize += len(text)
                        seen_texts[cache_key] = "pending"

    pct = (valid_count / total_required * 100) if total_required > 0 else 0
    print(f"\nAudit Summary for {chapter_basename}:")
    print(f"  Required Audio Files : {total_required}")
    print(f"  Valid Existing Files : {valid_count} ({pct:.1f}%)")
    print(f"  Missing Files        : {missing_count}")
    print(f"  Corrupted/Cleaned    : {corrupt_count}")
    print(f"  Points Already Spent : {already_spent_chars:,} points")
    print(f"  Dedup Points Saved   : {dedup_savings_chars:,} points")
    print(f"  Points to Complete   : {chars_to_synthesize:,} points")
    print(f"==================================================\n")

    return {
        "total_required": total_required,
        "valid": valid_count,
        "missing": missing_count,
        "corrupted": corrupt_count,
        "points_to_complete": chars_to_synthesize
    }

# ---------------------------------------------------------------------------
# Audio Generator Runner (with Checker, Dedup & Atomic Writing)
# ---------------------------------------------------------------------------
def generate_chapter_audio(
    chapter_dir: str,
    voices: Optional[List[str]] = None,
    item_types: Optional[List[str]] = None,
    skip_passages: bool = False,
    word_filter: Optional[int] = None,
    dry_run: bool = False,
    force: bool = False,
    delay: float = 0.25,
    client: Optional[MiniMaxAudioClient] = None
) -> dict:
    """Generates audio files for all words in a chapter with full duplicate prevention and checkers."""
    load_env_file()
    if client is None:
        client = MiniMaxAudioClient()

    if voices is None:
        env_voices = os.getenv("MINIMAX_VOICES")
        if env_voices:
            voices = list(VOICE_CONFIGS.keys()) if env_voices.lower() == 'all' else [v.strip() for v in env_voices.split(",") if v.strip()]
        else:
            # Option 1 default (Mature Woman + Office Man)
            voices = ["mature_woman", "office_man"]
    elif len(voices) == 1 and voices[0].lower() == 'all':
        voices = list(VOICE_CONFIGS.keys())
    else:
        for v in voices:
            if v not in VOICE_CONFIGS:
                print(f"[WARN] Unknown voice '{v}', using default configuration.")

    if not skip_passages:
        env_skip = os.getenv("MINIMAX_SKIP_PASSAGES", "").lower()
        if env_skip in ("true", "1", "yes"):
            skip_passages = True

    words_dir = os.path.join(chapter_dir, 'words')
    if not os.path.isdir(words_dir):
        print(f"[ERROR] Words directory not found: {words_dir}")
        return {"error": "words_dir_not_found"}

    audio_base_dir = os.path.join(chapter_dir, 'audio')
    os.makedirs(audio_base_dir, exist_ok=True)

    # Load persistent cross-word text cache for deduplication
    audio_cache = load_audio_cache(chapter_dir)

    words = parse_chapter(chapter_dir)
    if word_filter is not None:
        words = [w for w in words if int(w.get('id', -1)) == word_filter]
        if not words:
            print(f"[WARN] Word #{word_filter} not found in {chapter_dir}.")
            return {"generated": 0, "skipped": 0}

    stats = {
        "total_items": 0,
        "already_exists": 0,
        "dedup_reused": 0,
        "generated": 0,
        "failed": 0,
        "total_chars_synthesized": 0,
        "points_saved_by_dedup": 0
    }

    chapter_basename = os.path.basename(chapter_dir)
    print(f"\n==================================================")
    print(f"🎵 MiniMax Audio Generation for {chapter_basename}")
    print(f"Voices enabled   : {', '.join([VOICE_CONFIGS[v]['display_name'] for v in voices])}")
    print(f"Words to process : {len(words)}")
    print(f"Skip Passages    : {skip_passages}")
    print(f"Dry Run Mode     : {dry_run}")
    print(f"Force Overwrite  : {force}")
    print(f"Output Directory : {audio_base_dir}")
    print(f"==================================================")

    if not dry_run and not client.is_configured():
        print("\n❌ ERROR: MiniMax API Key is not configured!")
        print("Please create or edit the .env file in the repository root:")
        print("    MINIMAX_API_KEY=your_actual_minimax_api_key")
        print("\nYou can still run with '--dry-run' to inspect all audio files that will be generated.")
        return {"error": "api_key_missing"}

    for w_idx, w in enumerate(words, 1):
        w_id = int(w.get('id', w_idx))
        hanzi = w.get('hanzi', '')
        word_slug = f"{w_id:02d}_{hanzi}"
        word_audio_dir = os.path.join(audio_base_dir, word_slug)
        os.makedirs(word_audio_dir, exist_ok=True)

        items = extract_chinese_items(w)
        if skip_passages:
            items = [item for item in items if item[0] != 'passage']
        if item_types:
            items = [item for item in items if item[0] in item_types]

        print(f"\n[{w_idx}/{len(words)}] #{w_id:02d} {hanzi} ({len(items)} audio items):")

        for it_type, slug, text in items:
            for v_key in voices:
                voice_id = get_voice_id(v_key)
                out_filename = f"{slug}_{v_key}.mp3"
                out_path = os.path.join(word_audio_dir, out_filename)
                rel_out_path = os.path.join(word_slug, out_filename)
                cache_key = f"{text}___{v_key}"
                stats["total_items"] += 1

                # ---------------------------------------------------------------
                # Checker 1: File Existence & Integrity Check
                # ---------------------------------------------------------------
                if os.path.exists(out_path) and not force:
                    if is_valid_audio_file(out_path):
                        stats["already_exists"] += 1
                        # Register in cache if not present
                        if cache_key not in audio_cache:
                            audio_cache[cache_key] = rel_out_path
                        continue
                    else:
                        print(f"  [CHECKER]: Found corrupted/incomplete {out_filename}, re-generating...")
                        try:
                            os.remove(out_path)
                        except Exception:
                            pass

                # ---------------------------------------------------------------
                # Checker 2: Cross-Word Dedup Reuse (0 API Points!)
                # ---------------------------------------------------------------
                if cache_key in audio_cache and not force:
                    source_rel = audio_cache[cache_key]
                    source_full = os.path.join(audio_base_dir, source_rel)
                    if is_valid_audio_file(source_full):
                        if dry_run:
                            stats["dedup_reused"] += 1
                            stats["points_saved_by_dedup"] += len(text)
                            print(f"  [DRY RUN - DEDUP REUSE 0 PTS]: {word_slug}/{out_filename} (copied from {source_rel})")
                            continue

                        try:
                            shutil.copy2(source_full, out_path)
                            stats["dedup_reused"] += 1
                            stats["points_saved_by_dedup"] += len(text)
                            print(f"  [DEDUP REUSE - 0 PTS]: {word_slug}/{out_filename} ('{text}')")
                            continue
                        except Exception as e:
                            print(f"  [WARN] Copy failed, will synthesize: {e}")

                if dry_run:
                    print(f"  [DRY RUN - API CALL]: {word_slug}/{out_filename} (Voice: {v_key}, Text: '{text[:25]}{'...' if len(text)>25 else ''}')")
                    stats["generated"] += 1
                    stats["total_chars_synthesized"] += len(text)
                    audio_cache[cache_key] = rel_out_path
                    continue

                # ---------------------------------------------------------------
                # Live Synthesis via MiniMax with Atomic File Writing
                # ---------------------------------------------------------------
                try:
                    print(f"  [SYNTHESIZING]: {v_key} -> '{text[:20]}{'...' if len(text)>20 else ''}' ({len(text)} chars)...", end="", flush=True)
                    audio_bytes = client.synthesize(text=text, voice_id=voice_id)

                    # Strategy: Write to .tmp first and atomically rename
                    tmp_path = out_path + ".tmp"
                    with open(tmp_path, 'wb') as f:
                        f.write(audio_bytes)
                    os.replace(tmp_path, out_path)

                    # Register in persistent cache
                    audio_cache[cache_key] = rel_out_path

                    stats["generated"] += 1
                    stats["total_chars_synthesized"] += len(text)
                    print(f" OK ({len(audio_bytes)} bytes)")
                    time.sleep(delay)
                except Exception as e:
                    stats["failed"] += 1
                    print(f" FAILED: {e}")

    # Save updated persistent audio cache
    if not dry_run:
        save_audio_cache(chapter_dir, audio_cache)

    # Recompile chapter dataset so data.json & data.js instantly link audio paths
    if not dry_run and (stats["generated"] > 0 or stats["dedup_reused"] > 0):
        print(f"\n🔄 Compiling updated audio paths into {chapter_basename} datasets...")
        compile_chapter(chapter_dir)
        print(f"✓ Recompiled data.json and data.js with new audio references!")

    print(f"\n==================================================")
    print(f"Finished audio processing for {chapter_basename}:")
    print(f"  Total items checked : {stats['total_items']}")
    print(f"  Already existed     : {stats['already_exists']}")
    print(f"  Dedup reuses (0 pts): {stats['dedup_reused']} (saved {stats['points_saved_by_dedup']:,} points)")
    print(f"  Newly synthesized   : {stats['generated']}")
    print(f"  Failed              : {stats['failed']}")
    if not dry_run:
        print(f"  Points consumed     : {stats['total_chars_synthesized']:,}")
    print(f"==================================================")

    return stats
