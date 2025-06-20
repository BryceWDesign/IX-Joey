# jxcore/tests/test_context_switcher.py

import unittest
from jxcore.knowledge.block_manager import BlockManager
from jxcore.knowledge.context_switcher import ContextSwitcher

class DummyBlockManager(BlockManager):
    def __init__(self):
        self.loaded = []
    def load_block(self, block_name):
        self.loaded.append(block_name)
        return True
    def unload_block(self, block_name):
        if block_name in self.loaded:
            self.loaded.remove(block_name)
            return True
        return False

class TestContextSwitcher(unittest.TestCase):
    def setUp(self):
        self.block_manager = DummyBlockManager()
        self.context_map = {
            "medical": {"keywords": ["doctor", "medicine"], "blocks": ["med_block"]},
            "mechanical": {"keywords": ["engine", "wrench"], "blocks": ["mech_block"]}
        }
        self.cs = ContextSwitcher(self.block_manager, self.context_map)

    def test_detect_context(self):
        self.assertEqual(self.cs.detect_context("I need a doctor"), "medical")
        self.assertEqual(self.cs.detect_context("Fix the engine"), "mechanical")
        self.assertIsNone(self.cs.detect_context("No keyword here"))

    def test_switch_context(self):
        ctx = self.cs.switch_context("I need a doctor")
        self.assertEqual(ctx, "medical")
        self.assertIn("med_block", self.block_manager.loaded)

        ctx = self.cs.switch_context("Fix the engine")
        self.assertEqual(ctx, "mechanical")
        self.assertIn("mech_block", self.block_manager.loaded)
        self.assertNotIn("med_block", self.block_manager.loaded)

        # Switching to same context does nothing
        ctx = self.cs.switch_context("Fix the engine")
        self.assertEqual(ctx, "mechanical")
        self.assertIn("mech_block", self.block_manager.loaded)

if __name__ == "__main__":
    unittest.main()
