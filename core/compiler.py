import os
import re
import json
from .toon_parser import parse_chapter

VOICE_KEYS = ['mature_woman', 'soothing_host', 'office_man', 'tender_ceo']

def attach_audio_metadata(words: list, chapter_dir: str) -> None:
    """Scans chapter_dir/audio/ for generated MP3 files and attaches audio paths to words."""
    dirname = os.path.basename(os.path.abspath(chapter_dir))
    audio_base = os.path.join(chapter_dir, 'audio')

    if not os.path.isdir(audio_base):
        return

    for idx, w in enumerate(words, 1):
        w_id = int(w.get('id', idx))
        hanzi = w.get('hanzi', '')
        word_slug = f"{w_id:02d}_{hanzi}"
        word_audio_dir = os.path.join(audio_base, word_slug)

        if not os.path.isdir(word_audio_dir):
            continue

        rel_prefix = f"chapters/{dirname}/audio/{word_slug}"

        # 1. Headword
        hw_audio = {}
        for v in VOICE_KEYS:
            fn = f"headword_{v}.mp3"
            if os.path.isfile(os.path.join(word_audio_dir, fn)):
                hw_audio[v] = f"{rel_prefix}/{fn}"
        if hw_audio:
            w['audio'] = hw_audio

        # 2. Example sentences
        for s_idx, sent in enumerate(w.get('example_sentences', []), 1):
            sent_audio = {}
            for v in VOICE_KEYS:
                fn = f"sentence_{s_idx}_{v}.mp3"
                if os.path.isfile(os.path.join(word_audio_dir, fn)):
                    sent_audio[v] = f"{rel_prefix}/{fn}"
            if sent_audio:
                sent['audio'] = sent_audio

        # 3. Collocations
        for c_idx, c in enumerate(w.get('collocations', []), 1):
            colloc_audio = {}
            for v in VOICE_KEYS:
                fn = f"collocation_{c_idx}_{v}.mp3"
                if os.path.isfile(os.path.join(word_audio_dir, fn)):
                    colloc_audio[v] = f"{rel_prefix}/{fn}"
            if colloc_audio:
                c['audio'] = colloc_audio

        # 4. Idioms
        for i_idx, im in enumerate(w.get('idioms', []), 1):
            idiom_audio = {}
            for v in VOICE_KEYS:
                fn = f"idiom_{i_idx}_{v}.mp3"
                if os.path.isfile(os.path.join(word_audio_dir, fn)):
                    idiom_audio[v] = f"{rel_prefix}/{fn}"
            if idiom_audio:
                im['audio'] = idiom_audio

        # 5. Extended Reading Passages
        for p_idx, p in enumerate(w.get('extended_reading_passages', []), 1):
            passage_audio = {}
            for v in VOICE_KEYS:
                fn = f"passage_{p_idx}_{v}.mp3"
                if os.path.isfile(os.path.join(word_audio_dir, fn)):
                    passage_audio[v] = f"{rel_prefix}/{fn}"
            if passage_audio:
                p['audio'] = passage_audio

        # 6. Character decomposition
        for ch in w.get('character_decomposition', []):
            ch_char = ch.get('character', '').strip()
            if ch_char:
                char_audio = {}
                for v in VOICE_KEYS:
                    fn = f"char_{ch_char}_{v}.mp3"
                    if os.path.isfile(os.path.join(word_audio_dir, fn)):
                        char_audio[v] = f"{rel_prefix}/{fn}"
                if char_audio:
                    ch['audio'] = char_audio

        # 7. Look-alikes and Cognates
        tc = w.get('traps_and_cognates', {})
        for la in tc.get('look_alikes', []):
            la_char = la.get('character', '').strip()
            if la_char:
                la_audio = {}
                for v in VOICE_KEYS:
                    fn = f"lookalike_{la_char}_{v}.mp3"
                    if os.path.isfile(os.path.join(word_audio_dir, fn)):
                        la_audio[v] = f"{rel_prefix}/{fn}"
                if la_audio:
                    la['audio'] = la_audio

        for cg in tc.get('etymological_cognates', []):
            cg_char = cg.get('character', '').strip()
            if cg_char:
                cg_audio = {}
                for v in VOICE_KEYS:
                    fn = f"cognate_{cg_char}_{v}.mp3"
                    if os.path.isfile(os.path.join(word_audio_dir, fn)):
                        cg_audio[v] = f"{rel_prefix}/{fn}"
                if cg_audio:
                    cg['audio'] = cg_audio

def get_chapter_meta(chapter_dir: str, word_count: int) -> dict:
    """Infers metadata for a chapter from its directory and files."""
    dirname = os.path.basename(os.path.abspath(chapter_dir))
    m = re.search(r'chapter_?(\d+)', dirname, re.IGNORECASE)
    chapter_num = int(m.group(1)) if m else 1

    # Check for custom chapter_info.json
    info_path = os.path.join(chapter_dir, 'chapter_info.json')
    if os.path.exists(info_path):
        try:
            with open(info_path, 'r', encoding='utf-8') as f:
                info = json.load(f)
                return {
                    "id": chapter_num,
                    "dir": dirname,
                    "name": info.get("name", f"Chapter {chapter_num}"),
                    "title": info.get("title", ""),
                    "word_count": word_count,
                    "level": info.get("level", "HSK 5")
                }
        except Exception:
            pass

    # Fallback default metadata
    first_word_hanzi = ""
    words_dir = os.path.join(chapter_dir, 'words')
    if os.path.exists(words_dir):
        files = sorted([f for f in os.listdir(words_dir) if f.endswith('.toon')])
        if files:
            first_m = re.match(r'^\d+_(.+)\.toon$', files[0])
            if first_m:
                first_word_hanzi = first_m.group(1)

    title = f"HSK 5 Vocabulary ({first_word_hanzi}...)" if first_word_hanzi else "HSK 5 Vocabulary"
    if chapter_num == 1:
        title = "细节 (Details) & Everyday Relationships"

    return {
        "id": chapter_num,
        "dir": dirname,
        "name": f"Chapter {chapter_num}",
        "title": title,
        "word_count": word_count,
        "level": "HSK 5"
    }

def compile_chapter(chapter_dir: str) -> dict:
    """Compiles all .toon files in chapter_dir into data.json and data.js with audio links."""
    words = parse_chapter(chapter_dir)
    attach_audio_metadata(words, chapter_dir)
    meta = get_chapter_meta(chapter_dir, len(words))

    # Output data.json
    json_path = os.path.join(chapter_dir, 'data.json')
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(words, f, ensure_ascii=False, indent=2)

    # Output data.js for zero-server file:// browsing fallback
    js_path = os.path.join(chapter_dir, 'data.js')
    json_compact = json.dumps(words, ensure_ascii=False)
    with open(js_path, 'w', encoding='utf-8') as f:
        f.write(f"window.__HSK_CHAPTER_DATA__ = window.__HSK_CHAPTER_DATA__ || {{}};\n")
        f.write(f"window.__HSK_CHAPTER_DATA__['{meta['dir']}'] = {json_compact};\n")

    return meta

def compile_all(base_dir: str = ".") -> list[dict]:
    """Compiles all chapters under chapters/ and generates data/chapters.json."""
    chapters_root = os.path.join(base_dir, 'chapters')
    if not os.path.exists(chapters_root):
        os.makedirs(chapters_root, exist_ok=True)

    chapter_dirs = []
    for d in sorted(os.listdir(chapters_root)):
        full_p = os.path.join(chapters_root, d)
        if os.path.isdir(full_p) and re.match(r'^chapter_', d, re.IGNORECASE):
            chapter_dirs.append(full_p)

    manifest = []
    for cd in chapter_dirs:
        meta = compile_chapter(cd)
        manifest.append(meta)

    manifest.sort(key=lambda m: m['id'])

    # Write manifest to data/chapters.json and data/chapters.js
    data_dir = os.path.join(base_dir, 'data')
    os.makedirs(data_dir, exist_ok=True)

    manifest_json_path = os.path.join(data_dir, 'chapters.json')
    with open(manifest_json_path, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)

    manifest_js_path = os.path.join(data_dir, 'chapters.js')
    with open(manifest_js_path, 'w', encoding='utf-8') as f:
        f.write(f"window.__HSK_CHAPTERS_MANIFEST__ = {json.dumps(manifest, ensure_ascii=False, indent=2)};\n")

    return manifest
