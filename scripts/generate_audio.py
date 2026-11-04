#!/usr/bin/env python3
"""Standalone script to run MiniMax Audio Generation for Chinese Vocal HSK chapters."""

import os
import sys
import argparse

# Ensure project root is in sys.path
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from core.audio_generator import generate_chapter_audio, VOICE_CONFIGS
from cli import get_chapter_dir, list_all_chapter_dirs

def main():
    parser = argparse.ArgumentParser(
        description="Generate native Chinese audio using MiniMax TTS API across 4 voice personas."
    )
    parser.add_argument("--chapter", "-c", type=int, default=None, help="Chapter number (e.g. 1). Defaults to all.")
    parser.add_argument("--word", "-w", type=int, default=None, help="Specific word ID to generate (e.g. 1).")
    parser.add_argument("--voices", "-v", type=str, default=None,
                        help="Comma-separated voices: mature_woman,soothing_host,office_man,tender_ceo (default: all 4)")
    parser.add_argument("--items", "-i", type=str, default=None,
                        help="Comma-separated item types: headword,sentence,collocation,idiom,passage,char (default: all)")
    parser.add_argument("--dry-run", action="store_true", help="Preview planned generation without calling API.")
    parser.add_argument("--force", "-f", action="store_true", help="Overwrite existing audio files.")
    parser.add_argument("--delay", type=float, default=0.25, help="Delay between API requests in seconds (default: 0.25s).")

    args = parser.parse_args()

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

if __name__ == "__main__":
    sys.exit(main())
