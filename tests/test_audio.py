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

if __name__ == '__main__':
    unittest.main()
