import os
import re
import json
from .toon_parser import parse_chapter

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
    """Compiles all .toon files in chapter_dir into data.json and data.js."""
    words = parse_chapter(chapter_dir)
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
