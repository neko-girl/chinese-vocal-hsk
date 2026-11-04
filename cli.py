#!/usr/bin/env python3
"""Unified CLI for Chinese Vocal HSK Lexicographical Engine & Web Visualizer.

Commands:
  status        Check generation progress and pending words for a chapter
  validate      Validate schema compliance of .toon files
  build         Compile .toon files into web datasets (data.json & data.js)
  audio         Generate native Chinese audio using MiniMax TTS across 4 voices
  new-chapter   Scaffold a new chapter folder with vocabulary source
  prompt        Generate agent-ready prompt for a batch of words
  generate      Run batch generator scripts for a chapter
  serve         Start a local preview web server
"""

import os
import sys
import argparse
import re
import csv
import json
import http.server
import socketserver

from core.toon_validator import validate_chapter, validate_toon_file
from core.compiler import compile_chapter, compile_all
from core.audio_generator import generate_chapter_audio, VOICE_CONFIGS


BASE_DIR = os.path.abspath(os.path.dirname(__file__))

def get_chapter_dir(chapter_num: int) -> str:
    candidates = [
        os.path.join(BASE_DIR, 'chapters', f'chapter_{chapter_num:02d}'),
        os.path.join(BASE_DIR, 'chapters', f'chapter_{chapter_num}'),
        os.path.join(BASE_DIR, 'chapters', f'ch{chapter_num:02d}'),
        os.path.join(BASE_DIR, 'chapters', f'ch{chapter_num}')
    ]
    for c in candidates:
        if os.path.exists(c):
            return c
    return os.path.join(BASE_DIR, 'chapters', f'chapter_{chapter_num:02d}')

def list_all_chapter_dirs() -> list[str]:
    chapters_root = os.path.join(BASE_DIR, 'chapters')
    if not os.path.exists(chapters_root):
        return []
    dirs = []
    for d in sorted(os.listdir(chapters_root)):
        p = os.path.join(chapters_root, d)
        if os.path.isdir(p) and re.match(r'^(chapter_|ch)', d, re.IGNORECASE):
            dirs.append(p)
    return dirs

def cmd_status(args):
    """Check generation progress against vocabulary.csv."""
    if args.chapter is not None:
        dirs = [get_chapter_dir(args.chapter)]
    else:
        dirs = list_all_chapter_dirs()

    if not dirs:
        print("No chapters found in chapters/ directory.")
        return 0

    for cdir in dirs:
        dirname = os.path.basename(cdir)
        vocab_path = os.path.join(cdir, 'vocabulary.csv')
        words_dir = os.path.join(cdir, 'words')

        vocab_words = []
        if os.path.exists(vocab_path):
            with open(vocab_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                vocab_words = list(reader)

        existing_files = set()
        if os.path.exists(words_dir):
            existing_files = {f for f in os.listdir(words_dir) if f.endswith('.toon')}

        total_vocab = len(vocab_words)
        total_generated = len(existing_files)
        pct = (total_generated / total_vocab * 100) if total_vocab > 0 else 0

        print(f"\n==================================================")
        print(f"Status for {dirname}:")
        print(f"Vocabulary source : {total_vocab} words ({vocab_path if os.path.exists(vocab_path) else 'None'})")
        print(f"Generated .toon   : {total_generated} / {total_vocab} ({pct:.1f}%)")

        # Validate generated
        valid_count = 0
        invalid_files = []
        for f in existing_files:
            errs = validate_toon_file(os.path.join(words_dir, f))
            if not errs:
                valid_count += 1
            else:
                invalid_files.append((f, errs))

        print(f"Valid schema      : {valid_count} / {total_generated}")
        if invalid_files:
            print(f"Invalid files ({len(invalid_files)}):")
            for f, errs in invalid_files[:5]:
                print(f"  - {f}: {errs[0]}")
            if len(invalid_files) > 5:
                print(f"  ... and {len(invalid_files)-5} more.")

        # Find pending words
        if vocab_words:
            pending = []
            for row in vocab_words:
                no = row.get('No') or row.get('id') or row.get('ID')
                hanzi = row.get('Hanzi') or row.get('hanzi')
                expected_filename = f"{int(no):02d}_{hanzi}.toon"
                if expected_filename not in existing_files:
                    pending.append(row)

            if pending:
                print(f"\nPending Words ({len(pending)} remaining):")
                batch_size = args.batch_size or 5
                next_batch = pending[:batch_size]
                print(f"  --> Next batch recommendation (Batch size {batch_size}):")
                for row in next_batch:
                    no = row.get('No') or row.get('id')
                    hanzi = row.get('Hanzi')
                    pinyin = row.get('Pinyin', '')
                    meaning = row.get('Meaning', '')
                    print(f"      #{no:>2} {hanzi} ({pinyin}) - {meaning}")
            else:
                print("\n  All vocabulary words have been generated!")

    return 0

def cmd_validate(args):
    """Validate schema compliance of .toon files."""
    if args.chapter is not None:
        dirs = [get_chapter_dir(args.chapter)]
    else:
        dirs = list_all_chapter_dirs()

    if not dirs:
        print("No chapters found to validate.")
        return 1

    overall_ok = True
    for cdir in dirs:
        dirname = os.path.basename(cdir)
        print(f"\n--- Validating {dirname} ({cdir}) ---")
        ok, results = validate_chapter(cdir)
        if ok:
            words_count = len([k for k in results if not k.startswith('_')])
            print(f"[PASS] All {words_count} .toon files in {dirname} are strictly valid!")
        else:
            overall_ok = False
            for f, errs in results.items():
                if errs:
                    print(f"[FAIL] {f}:")
                    for e in errs:
                        print(f"  - {e}")

    return 0 if overall_ok else 1

def cmd_build(args):
    """Compile .toon files into JSON datasets and manifest."""
    if args.chapter is not None:
        cdir = get_chapter_dir(args.chapter)
        if not os.path.exists(cdir):
            print(f"Error: Chapter directory does not exist: {cdir}")
            return 1
        meta = compile_chapter(cdir)
        print(f"Compiled {meta['dir']}: {meta['word_count']} words.")
        # Update global manifest as well
        compile_all(BASE_DIR)
        print("Updated data/chapters.json manifest.")
    else:
        manifest = compile_all(BASE_DIR)
        print(f"Compiled all chapters ({len(manifest)} total chapters).")
        for m in manifest:
            print(f"  - {m['name']} ({m['dir']}): {m['word_count']} words")
        print("Manifest written to data/chapters.json and data/chapters.js")
    return 0

def cmd_new_chapter(args):
    """Scaffold a new chapter folder with vocabulary source."""
    ch_num = args.number
    csv_path = args.csv_path
    if not os.path.exists(csv_path):
        print(f"Error: Vocabulary CSV file not found: {csv_path}")
        return 1

    target_dir = os.path.join(BASE_DIR, 'chapters', f'chapter_{ch_num:02d}')
    if os.path.exists(target_dir):
        print(f"Error: Chapter directory already exists: {target_dir}")
        return 1

    words_dir = os.path.join(target_dir, 'words')
    generators_dir = os.path.join(target_dir, 'generators')
    os.makedirs(words_dir, exist_ok=True)
    os.makedirs(generators_dir, exist_ok=True)

    # Copy CSV
    dest_csv = os.path.join(target_dir, 'vocabulary.csv')
    with open(csv_path, 'r', encoding='utf-8') as src, open(dest_csv, 'w', encoding='utf-8') as dst:
        dst.write(src.read())

    # Write chapter_info.json
    title = args.title or f"Chapter {ch_num} Vocabulary"
    info = {
        "id": ch_num,
        "name": f"Chapter {ch_num}",
        "title": title,
        "level": "HSK 5",
        "description": f"HSK 5 vocabulary dataset for Chapter {ch_num}"
    }
    with open(os.path.join(target_dir, 'chapter_info.json'), 'w', encoding='utf-8') as f:
        json.dump(info, f, ensure_ascii=False, indent=2)

    print(f"Successfully scaffolded new chapter:")
    print(f"  Directory: {target_dir}")
    print(f"  Vocabulary: {dest_csv}")
    print(f"  Words folder: {words_dir}")
    print(f"\nNext steps for the agent or user:")
    print(f"  1. Run `python cli.py status --chapter {ch_num}` to inspect vocabulary words.")
    print(f"  2. Run `python cli.py prompt --chapter {ch_num} --batch 1` to generate prompt.")
    print(f"  3. Write .toon files directly into `chapters/chapter_{ch_num:02d}/words/`.")
    print(f"  4. Run `python cli.py validate --chapter {ch_num}` to verify schema compliance.")
    print(f"  5. Run `python cli.py build --chapter {ch_num}` to compile into the web visualizer.")
    return 0

def cmd_prompt(args):
    """Generate prompt text for an AI agent to generate a batch of words."""
    cdir = get_chapter_dir(args.chapter)
    vocab_path = os.path.join(cdir, 'vocabulary.csv')
    if not os.path.exists(vocab_path):
        print(f"Error: vocabulary.csv not found in {cdir}")
        return 1

    with open(vocab_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        vocab = list(reader)

    words_dir = os.path.join(cdir, 'words')
    existing = set(os.listdir(words_dir)) if os.path.exists(words_dir) else set()

    pending = []
    for row in vocab:
        no = row.get('No') or row.get('id')
        hanzi = row.get('Hanzi')
        fname = f"{int(no):02d}_{hanzi}.toon"
        if fname not in existing:
            pending.append(row)

    batch_size = args.batch_size or 5
    if args.batch is not None:
        start_idx = (args.batch - 1) * batch_size
        batch_words = vocab[start_idx:start_idx + batch_size]
    else:
        batch_words = pending[:batch_size]

    if not batch_words:
        print("No pending words found for this batch!")
        return 0

    ch_basename = os.path.basename(cdir)
    print(f"# AGENT TASK PROMPT: {ch_basename} (Batch of {len(batch_words)} words)")
    print("=" * 60)
    print("You are an expert Chinese-English-Spanish computational lexicographer.")
    print(f"Generate standalone .toon files for the following {len(batch_words)} words.")
    print(f"Target Directory: chapters/{ch_basename}/words/{{No_padded}}_{{Hanzi}}.toon\n")
    print("WORDS TO GENERATE:")
    for w in batch_words:
        print(f"- No: {w.get('No')}, Hanzi: {w.get('Hanzi')}, Pinyin: {w.get('Pinyin')}, POS: {w.get('Part_of_Speech')}, Meaning: {w.get('Meaning')}")

    print("\nSCHEMA RULES (Refer to tasks.md for exact specifications):")
    print("1. One standalone file per word: chapters/{ch_basename}/words/{No_padded}_{Hanzi}.toon")
    print("2. Required tables:")
    print("   - senses[M]{sense_number,part_of_speech,register,definition_en,definition_es,example_phrase}:")
    print("   - example_sentences[2]{id,hanzi,pinyin,en,es}:")
    print("   - collocations[6]{hanzi,en}:")
    print("   - idioms[4]{hanzi,pinyin,meaning_en}:")
    print("   - character_decomposition[K]{character,pinyin,meaning_en,meaning_es,radical,radical_meaning_en,meaning_component,sound_component,stroke_count,composition_type,etymology_and_mnemonic,visual_mnemonic_story_en,visual_mnemonic_story_es,tone_mnemonic_anchor,cangjie,traditional}:")
    print("   - mnemonics_and_roots (composite_memory_hook_en/es, cultural_and_cognitive_roots, tone_sandhi_and_pitch_modulation)")
    print("   - traps_and_cognates: look_alikes[4..6] and etymological_cognates[4..7]")
    print("   - semantic_boundary_contrasts: core_nuance and contrasts[3]")
    print("   - extended_reading_passages[2]: Passage #1 (50-80 Hanzi) & Passage #2 (60-90 Hanzi)")
    print("3. Validate immediately using: python cli.py validate --chapter " + str(args.chapter))
    print("=" * 60)
    return 0

def cmd_generate(args):
    """Run generator scripts for a chapter."""
    cdir = get_chapter_dir(args.chapter)
    gen_run = os.path.join(cdir, 'generators', 'run.py')
    if not os.path.exists(gen_run):
        print(f"No generators/run.py script found in {cdir}.")
        print("Note: In the new architecture, agents can write .toon files directly into words/.")
        return 1

    import subprocess
    cmd = [sys.executable, gen_run]
    print(f"Executing: {' '.join(cmd)}")
    return subprocess.call(cmd)

def cmd_audio(args):
    """Generate native Chinese audio using MiniMax TTS API across 4 voices."""
    voice_list = [v.strip() for v in args.voices.split(",")] if args.voices else None
    item_list = [it.strip() for it in args.items.split(",")] if args.items else None

    if args.chapter is not None:
        target_dirs = [get_chapter_dir(args.chapter)]
    else:
        target_dirs = list_all_chapter_dirs()

    if not target_dirs:
        print("No chapters found in chapters/ directory.")
        return 1

    for cdir in target_dirs:
        generate_chapter_audio(
            chapter_dir=cdir,
            voices=voice_list,
            item_types=item_list,
            word_filter=args.word,
            dry_run=args.dry_run,
            force=args.force,
            delay=args.delay
        )
    return 0

def cmd_serve(args):
    """Start local preview HTTP server."""
    port = args.port or 8000
    os.chdir(BASE_DIR)
    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", port), handler) as httpd:
        print(f"Serving Chinese Vocal HSK Visualizer at:")
        print(f"  http://localhost:{port}/")
        print(f"Press Ctrl+C to stop.")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")
    return 0

def main():
    parser = argparse.ArgumentParser(description="Chinese Vocal HSK Tooling & Lexicographical CLI")
    subparsers = parser.add_subparsers(dest="command", help="Subcommand to run")

    # status
    p_status = subparsers.add_parser("status", help="Check generation progress and pending words")
    p_status.add_argument("--chapter", "-c", type=int, help="Chapter number (e.g. 1)")
    p_status.add_argument("--batch-size", "-b", type=int, default=5, help="Batch size for pending words")

    # validate
    p_val = subparsers.add_parser("validate", help="Validate schema of .toon files")
    p_val.add_argument("--chapter", "-c", type=int, help="Chapter number (default: all)")

    # build
    p_build = subparsers.add_parser("build", help="Compile .toon files into JSON datasets & manifest")
    p_build.add_argument("--chapter", "-c", type=int, help="Chapter number (default: all)")

    # audio
    p_audio = subparsers.add_parser("audio", help="Generate Chinese audio using MiniMax TTS API (4 voices)")
    p_audio.add_argument("--chapter", "-c", type=int, help="Chapter number (default: all)")
    p_audio.add_argument("--word", "-w", type=int, help="Specific word ID (e.g. 1)")
    p_audio.add_argument("--voices", "-v", type=str, help="Comma-separated voices: mature_woman,soothing_host,office_man,tender_ceo")
    p_audio.add_argument("--items", "-i", type=str, help="Comma-separated item types: headword,sentence,collocation,idiom,passage,char")
    p_audio.add_argument("--dry-run", action="store_true", help="Preview planned generation without calling API")
    p_audio.add_argument("--force", "-f", action="store_true", help="Overwrite existing audio files")
    p_audio.add_argument("--delay", type=float, default=0.25, help="Delay between API calls in seconds (default: 0.25)")

    # new-chapter
    p_new = subparsers.add_parser("new-chapter", help="Scaffold a new chapter directory")
    p_new.add_argument("number", type=int, help="Chapter number (e.g. 2)")
    p_new.add_argument("csv_path", type=str, help="Path to vocabulary CSV file")
    p_new.add_argument("--title", "-t", type=str, help="Chapter title / theme description")

    # prompt
    p_prompt = subparsers.add_parser("prompt", help="Generate prompt for agent to generate next batch")
    p_prompt.add_argument("--chapter", "-c", type=int, required=True, help="Chapter number")
    p_prompt.add_argument("--batch", "-b", type=int, help="Batch number (1-based)")
    p_prompt.add_argument("--batch-size", "-s", type=int, default=5, help="Batch size")

    # generate
    p_gen = subparsers.add_parser("generate", help="Run chapter generator scripts")
    p_gen.add_argument("--chapter", "-c", type=int, required=True, help="Chapter number")

    # serve
    p_serve = subparsers.add_parser("serve", help="Start local web server")
    p_serve.add_argument("--port", "-p", type=int, default=8000, help="Port (default: 8000)")

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        return 0

    commands = {
        "status": cmd_status,
        "validate": cmd_validate,
        "build": cmd_build,
        "audio": cmd_audio,
        "new-chapter": cmd_new_chapter,
        "prompt": cmd_prompt,
        "generate": cmd_generate,
        "serve": cmd_serve
    }

    return commands[args.command](args)

if __name__ == '__main__':
    sys.exit(main())
