# jxcore/tests/test_core_loop.py

import unittest
from jxcore.core_loop import JXCore

class TestJXCore(unittest.TestCase):
    def setUp(self):
        self.root_map = {
            "ran": "run", "running": "run", "dogs": "dog",
            "eats": "eat", "ate": "eat", "apples": "apple",
            "quickly": "quick", "happily": "happy", "sang": "sing"
        }

        self.morph_bank = {
            "run": {"meaning": "to move fast", "type": "verb"},
            "eat": {"meaning": "to consume", "type": "verb"},
            "dog": {"meaning": "domesticated animal", "type": "noun"},
            "apple": {"meaning": "fruit", "type": "noun"},
            "quick": {"meaning": "fast", "type": "adverb"},
            "happy": {"meaning": "joyful", "type": "adverb"},
            "sing": {"meaning": "vocalize music", "type": "verb"},
            "cat": {"meaning": "feline animal", "type": "noun"}
        }

        self.semantic_patterns = {}  # optional advanced use

        self.jx = JXCore(self.root_map, self.morph_bank, self.semantic_patterns)

    def test_parse_input(self):
        parsed = self.jx.parse_input("The dog ran quickly")
        self.assertEqual(parsed[1]["root"], "dog")
        self.assertEqual(parsed[2]["root"], "run")
        self.assertEqual(parsed[3]["type"], "adverb")

    def test_extract_pattern(self):
        parsed = self.jx.parse_input("The dog ran quickly")
        pattern = self.jx.extract_pattern(parsed)
        self.assertEqual(pattern["who"], "dog")
        self.assertEqual(pattern["does"], "ran")
        self.assertEqual(pattern["modifiers"][0], "quickly")

    def test_respond(self):
        pattern = {
            "who": "cat",
            "does": "eat",
            "what": "apple",
            "modifiers": []
        }
        reply = self.jx.respond(pattern)
        self.assertEqual(reply, "cat eat apple")

    def test_end_to_end(self):
        response = self.jx.think("A cat eats an apple")
        self.assertIn("cat", response)
        self.assertIn("eat", response)
        self.assertIn("apple", response)

if __name__ == "__main__":
    unittest.main()
