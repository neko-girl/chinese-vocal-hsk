"""MiniMax Text-to-Speech (T2A v2) Audio Generator for Chinese Vocal HSK.

Generates native Chinese audio for vocabulary headwords, sentences, collocations,
idioms, reading passages, and characters using 4 distinct MiniMax voice personas:
  1. Mature Woman (成熟女性)
  2. Soothing Host (温润女主播 / 播音主持)
  3. Office Man (职场男音 / 精英青年)
  4. Tender CEO (温润/霸道总裁)
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
        """Synthesizes text to MP3 bytes via MiniMax T2A v2 API.
        
        Args:
            text: The Chinese text string to synthesize.
            voice_id: The MiniMax system or cloned voice ID.
            speed: Speech speed multiplier (default 1.0).
            
        Returns:
            Raw MP3 bytes.
        """
        if not self.is_configured():
            raise ValueError(
                "MINIMAX_API_KEY is not set. Please add it to your .env file or environment.\n"
                "Example: MINIMAX_API_KEY=your_key_here"
            )

        # Build endpoint URL (include GroupId query param if present)
        endpoint = f"{self.api_base}/t2a_v2"
        if self.group_id:
            endpoint += f"?GroupId={self.group_id}"

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        # Filter out non-Chinese/punctuation symbols if needed, preserving standard Chinese
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

        # Check MiniMax business status
        base_resp = resp_json.get("base_resp", {})
        status_code = base_resp.get("status_code", 0)
        status_msg = base_resp.get("status_msg", "")
        if status_code != 0:
            raise RuntimeError(f"MiniMax synthesis failed [Code {status_code}]: {status_msg}")

        audio_hex = resp_json.get("data", {}).get("audio", "")
        if not audio_hex:
            raise RuntimeError(f"MiniMax returned no audio data: {resp_json}")

        # Convert hex stream to binary MP3
        return bytes.fromhex(audio_hex)

# ---------------------------------------------------------------------------
# Word Item Extractor
# ---------------------------------------------------------------------------
def extract_chinese_items(word_data: dict) -> List[Tuple[str, str, str]]:
    """Extracts all Chinese text items that require audio from a word dictionary.
    
    Returns:
        List of tuples: (item_type, file_slug, chinese_text)
        e.g. ("headword", "headword", "细节")
             ("sentence", "sentence_1", "老艺术家的画作细腻生动...")
             ("collocation", "collocation_1", "注意细节")
             ("idiom", "idiom_1", "不拘小节")
             ("passage", "passage_1", "生活的美好往往隐藏在...")
             ("char", "char_细", "细")
    """
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
# Audio Generator Runner
# ---------------------------------------------------------------------------
def generate_chapter_audio(
    chapter_dir: str,
    voices: Optional[List[str]] = None,
    item_types: Optional[List[str]] = None,
    word_filter: Optional[int] = None,
    dry_run: bool = False,
    force: bool = False,
    delay: float = 0.25,
    client: Optional[MiniMaxAudioClient] = None
) -> dict:
    """Generates audio files for all words in a chapter across the 4 voices.
    
    Args:
        chapter_dir: Path to chapters/chapter_XX
        voices: List of voice keys (defaults to all 4 voices)
        item_types: Filter for item types (e.g. ['headword', 'sentence']) or None for all
        word_filter: Optional specific word ID to generate for
        dry_run: If True, only calculate and display planned generations without calling API
        force: If True, overwrite existing audio files
        delay: Sleep delay in seconds between API requests
        client: MiniMaxAudioClient instance
        
    Returns:
        Summary dict of execution stats.
    """
    load_env_file()
    if client is None:
        client = MiniMaxAudioClient()

    if voices is None:
        voices = list(VOICE_CONFIGS.keys())
    else:
        # Validate voices
        for v in voices:
            if v not in VOICE_CONFIGS:
                print(f"[WARN] Unknown voice '{v}', using default configuration.")

    words_dir = os.path.join(chapter_dir, 'words')
    if not os.path.isdir(words_dir):
        print(f"[ERROR] Words directory not found: {words_dir}")
        return {"error": "words_dir_not_found"}

    # Base audio directory for chapter: chapters/chapter_XX/audio/
    audio_base_dir = os.path.join(chapter_dir, 'audio')
    os.makedirs(audio_base_dir, exist_ok=True)

    # In-memory single-character cache to avoid paying duplicate API tokens
    # Key: (character, voice_key) -> raw bytes
    char_cache: Dict[Tuple[str, str], bytes] = {}

    words = parse_chapter(chapter_dir)
    if word_filter is not None:
        words = [w for w in words if int(w.get('id', -1)) == word_filter]
        if not words:
            print(f"[WARN] Word #{word_filter} not found in {chapter_dir}.")
            return {"generated": 0, "skipped": 0}

    stats = {
        "total_items": 0,
        "already_exists": 0,
        "generated": 0,
        "cached_reuse": 0,
        "failed": 0,
        "total_chars_synthesized": 0
    }

    chapter_basename = os.path.basename(chapter_dir)
    print(f"\n==================================================")
    print(f"🎵 MiniMax Audio Generation for {chapter_basename}")
    print(f"Voices enabled   : {', '.join([VOICE_CONFIGS[v]['display_name'] for v in voices])}")
    print(f"Words to process : {len(words)}")
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
        if item_types:
            items = [item for item in items if item[0] in item_types]

        print(f"\n[{w_idx}/{len(words)}] #{w_id:02d} {hanzi} ({len(items)} audio items):")

        for it_type, slug, text in items:
            for v_key in voices:
                v_cfg = VOICE_CONFIGS[v_key]
                voice_id = get_voice_id(v_key)
                out_filename = f"{slug}_{v_key}.mp3"
                out_path = os.path.join(word_audio_dir, out_filename)
                stats["total_items"] += 1

                # Check if file exists
                if os.path.exists(out_path) and not force and os.path.getsize(out_path) > 0:
                    stats["already_exists"] += 1
                    continue

                if dry_run:
                    print(f"  [DRY RUN] Will generate: {word_slug}/{out_filename} (Voice: {v_key}, Text: '{text[:25]}{'...' if len(text)>25 else ''}')")
                    stats["generated"] += 1
                    stats["total_chars_synthesized"] += len(text)
                    continue

                # Check single-character deduplication cache
                if it_type in ('char', 'lookalike', 'cognate') and len(text) == 1:
                    cache_key = (text, v_key)
                    if cache_key in char_cache:
                        with open(out_path, 'wb') as f:
                            f.write(char_cache[cache_key])
                        stats["cached_reuse"] += 1
                        stats["generated"] += 1
                        print(f"  [CACHE REUSE] {word_slug}/{out_filename} ('{text}')")
                        continue

                # Live API Call
                try:
                    print(f"  [SYNTHESIZING] {v_key} -> '{text[:22]}{'...' if len(text)>22 else ''}' ({len(text)} chars)...", end="", flush=True)
                    audio_bytes = client.synthesize(text=text, voice_id=voice_id)
                    with open(out_path, 'wb') as f:
                        f.write(audio_bytes)

                    # Store in cache if single character
                    if it_type in ('char', 'lookalike', 'cognate') and len(text) == 1:
                        char_cache[(text, v_key)] = audio_bytes

                    stats["generated"] += 1
                    stats["total_chars_synthesized"] += len(text)
                    print(f" OK ({len(audio_bytes)} bytes)")
                    time.sleep(delay)
                except Exception as e:
                    stats["failed"] += 1
                    print(f" FAILED: {e}")

    # Recompile chapter dataset so data.json & data.js instantly link audio paths
    if not dry_run and stats["generated"] > 0:
        print(f"\n🔄 Compiling updated audio paths into {chapter_basename} datasets...")
        compile_chapter(chapter_dir)
        print(f"✓ Recompiled data.json and data.js with new audio references!")

    print(f"\n==================================================")
    print(f"Finished audio processing for {chapter_basename}:")
    print(f"  Total items checked : {stats['total_items']}")
    print(f"  Already existed     : {stats['already_exists']}")
    print(f"  Generated           : {stats['generated']}")
    print(f"  Cache reuses        : {stats['cached_reuse']}")
    print(f"  Failed              : {stats['failed']}")
    if not dry_run:
        print(f"  Chars synthesized   : {stats['total_chars_synthesized']}")
    print(f"==================================================")

    return stats
