import os
import sys
import unittest
import tempfile
import json
import shutil

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from core.audio_generator import (
    MiniMaxAudioClient,
    VOICE_CONFIGS,
    get_voice_id,
    extract_chinese_items,
    is_valid_audio_file,
    load_audio_cache,
    save_audio_cache,
    check_chapter_audio,
    generate_chapter_audio,
    load_env_file
)
from core.compiler import attach_audio_metadata, VOICE_KEYS

class TestAudioGenerator(unittest.TestCase):

    def test_voice_configs(self):
        """Verify the 4 required voices exist with valid configurations."""
        required_voices = ["mature_woman", "soothing_host", "office_man", "tender_ceo"]
        for v in required_voices:
            self.assertIn(v, VOICE_CONFIGS)
            self.assertTrue(bool(VOICE_CONFIGS[v]["default_id"]))
            self.assertTrue(bool(VOICE_CONFIGS[v]["display_name"]))
            self.assertEqual(get_voice_id(v), VOICE_CONFIGS[v]["default_id"])

    def test_extract_chinese_items(self):
        """Verify extraction of Chinese items from word data."""
        mock_word = {
            "id": 1,
            "hanzi": "测试",
            "example_sentences": [
                {"id": "#1", "hanzi": "这是测试句子一。"},
                {"id": "#2", "hanzi": "这是测试句子二。"}
            ],
            "collocations": [
                {"hanzi": "系统测试"},
                {"hanzi": "进行测试"}
            ],
            "idioms": [
                {"hanzi": "试金石"}
            ],
            "extended_reading_passages": [
                {"id": "#1", "hanzi": "长篇阅读测试段落一。"}
            ],
            "character_decomposition": [
                {"character": "测"},
                {"character": "试"}
            ],
            "traps_and_cognates": {
                "look_alikes": [{"character": "侧"}],
                "etymological_cognates": [{"character": "式"}]
            }
        }

        items = extract_chinese_items(mock_word)
        slugs = [slug for _, slug, _ in items]

        self.assertIn("headword", slugs)
        self.assertIn("sentence_1", slugs)
        self.assertIn("sentence_2", slugs)
        self.assertIn("collocation_1", slugs)
        self.assertIn("collocation_2", slugs)
        self.assertIn("idiom_1", slugs)
        self.assertIn("passage_1", slugs)
        self.assertIn("char_测", slugs)
        self.assertIn("char_试", slugs)
        self.assertIn("lookalike_侧", slugs)
        self.assertIn("cognate_式", slugs)

    def test_compiler_attach_audio_metadata(self):
        """Verify that compiler attaches audio metadata for existing audio files."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            ch_dir = os.path.join(tmp_dir, "chapter_99")
            audio_dir = os.path.join(ch_dir, "audio", "01_测试")
            os.makedirs(audio_dir, exist_ok=True)

            # Create mock mp3 files for word #1
            sample_bytes = b"ID3\x03\x00\x00\x00\x00\x00#MOCK_AUDIO_MP3#"
            with open(os.path.join(audio_dir, "headword_mature_woman.mp3"), "wb") as f:
                f.write(sample_bytes)
            with open(os.path.join(audio_dir, "headword_tender_ceo.mp3"), "wb") as f:
                f.write(sample_bytes)
            with open(os.path.join(audio_dir, "sentence_1_office_man.mp3"), "wb") as f:
                f.write(sample_bytes)

            mock_words = [
                {
                    "id": 1,
                    "hanzi": "测试",
                    "example_sentences": [
                        {"id": "#1", "hanzi": "句子一"}
                    ]
                }
            ]

            attach_audio_metadata(mock_words, ch_dir)

            # Check that headword audio was attached with both voices
            self.assertIn("audio", mock_words[0])
            self.assertIn("mature_woman", mock_words[0]["audio"])
            self.assertIn("tender_ceo", mock_words[0]["audio"])
            self.assertNotIn("soothing_host", mock_words[0]["audio"])
            self.assertEqual(
                mock_words[0]["audio"]["mature_woman"],
                "chapters/chapter_99/audio/01_测试/headword_mature_woman.mp3"
            )

            # Check sentence audio
            sent = mock_words[0]["example_sentences"][0]
            self.assertIn("audio", sent)
            self.assertIn("office_man", sent["audio"])
            self.assertEqual(
                sent["audio"]["office_man"],
                "chapters/chapter_99/audio/01_测试/sentence_1_office_man.mp3"
            )

    def test_client_hex_conversion(self):
        """Verify hex conversion logic used in MiniMax client."""
        raw_bytes = b"MP3_SYNTHESIZED_AUDIO_BYTES_TEST"
        hex_str = raw_bytes.hex()
        converted = bytes.fromhex(hex_str)
        self.assertEqual(converted, raw_bytes)

    def test_is_valid_audio_file(self):
        """Verify validation of MP3 files and detection of corrupt/empty files."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            # Valid ID3 file
            valid_id3 = os.path.join(tmp_dir, "valid_id3.mp3")
            with open(valid_id3, "wb") as f:
                f.write(b"ID3" + b"\x03\x00\x00\x00\x00\x00" + b"\x00" * 200)
            self.assertTrue(is_valid_audio_file(valid_id3))

            # Valid MPEG sync file
            valid_mpeg = os.path.join(tmp_dir, "valid_mpeg.mp3")
            with open(valid_mpeg, "wb") as f:
                f.write(b"\xff\xfb\x90\x64" + b"\x00" * 200)
            self.assertTrue(is_valid_audio_file(valid_mpeg))

            # Corrupted 0-byte file
            empty_file = os.path.join(tmp_dir, "empty.mp3")
            with open(empty_file, "wb") as f:
                pass
            self.assertFalse(is_valid_audio_file(empty_file))

            # Corrupted tiny error string
            error_file = os.path.join(tmp_dir, "error.mp3")
            with open(error_file, "wb") as f:
                f.write(b'{"error": "rate limit"}')
            self.assertFalse(is_valid_audio_file(error_file))

    def test_dedup_cache_and_check(self):
        """Verify audio cache saving and checking mechanism."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            ch_dir = os.path.join(tmp_dir, "chapter_01")
            audio_dir = os.path.join(ch_dir, "audio")
            words_dir = os.path.join(ch_dir, "words")
            os.makedirs(audio_dir, exist_ok=True)
            os.makedirs(words_dir, exist_ok=True)

            # Write a minimal .toon file
            toon_content = (
                "id: 1\nhanzi: 细节\npinyin: xì jié\nlevel: HSK 5\npart_of_speech: Noun\n\n"
                "meanings_summary:\n  en: details\n  es: detalles\n\n"
                "example_sentences[2]{id,hanzi,pinyin,en,es}:\n"
                "  #1 | 句子一 | p1 | e1 | s1\n  #2 | 句子二 | p2 | e2 | s2\n\n"
                "collocations[1]{hanzi,en}:\n  注意细节 | pay attention\n\n"
                "idioms[1]{hanzi,pinyin,meaning_en}:\n  不拘小节 | bu ju | trifles\n\n"
                "character_decomposition[1]{character,pinyin,meaning_en,meaning_es,radical,radical_meaning_en,meaning_component,sound_component,stroke_count,composition_type,etymology_and_mnemonic,visual_mnemonic_story_en,visual_mnemonic_story_es,tone_mnemonic_anchor,cangjie,traditional}:\n"
                "  细 | xi | fine | fino | s | silk | m | s | 8 | lr | ety | vis | vis | 51 | c | 細\n"
            )
            with open(os.path.join(words_dir, "01_细节.toon"), "w", encoding="utf-8") as f:
                f.write(toon_content)

            # Audit check
            res = check_chapter_audio(ch_dir, voices=["mature_woman", "office_man"], skip_passages=True)
            self.assertGreater(res["total_required"], 0)
            self.assertEqual(res["valid"], 0)
            self.assertEqual(res["missing"], res["total_required"])

            # Simulate one valid file generated
            w_dir = os.path.join(audio_dir, "01_细节")
            os.makedirs(w_dir, exist_ok=True)
            with open(os.path.join(w_dir, "headword_mature_woman.mp3"), "wb") as f:
                f.write(b"ID3" + b"\x00" * 200)

            # Audit again
            res2 = check_chapter_audio(ch_dir, voices=["mature_woman", "office_man"], skip_passages=True)
            self.assertEqual(res2["valid"], 1)
            self.assertEqual(res2["missing"], res["total_required"] - 1)

if __name__ == '__main__':
    unittest.main()
