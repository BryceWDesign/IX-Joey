# jxcore/tests/test_block_manager.py

import unittest
import os
from jxcore.knowledge.block_manager import BlockManager

class TestBlockManager(unittest.TestCase):
    def setUp(self):
        self.test_dir = "test_blocks"
        os.makedirs(self.test_dir, exist_ok=True)
        self.bm = BlockManager(blocks_dir=self.test_dir)
        # Create dummy block file
        with open(os.path.join(self.test_dir, "testblock.json"), "w", encoding="utf-8") as f:
            f.write('{"key1": "value1", "key2": [1,2,3]}')

    def tearDown(self):
        for f in os.listdir(self.test_dir):
            os.remove(os.path.join(self.test_dir, f))
        os.rmdir(self.test_dir)

    def test_load_and_unload(self):
        self.assertTrue(self.bm.load_block("testblock"))
        self.assertIn("testblock", self.bm.list_active_blocks())
        block = self.bm.get_block("testblock")
        self.assertIsNotNone(block)
        self.assertEqual(block["key1"], "value1")

        self.assertTrue(self.bm.unload_block("testblock"))
        self.assertNotIn("testblock", self.bm.list_active_blocks())
        self.assertIsNone(self.bm.get_block("testblock"))

    def test_reload_block(self):
        self.bm.load_block("testblock")
        self.assertTrue(self.bm.reload_block("testblock"))
        self.assertIn("testblock", self.bm.list_active_blocks())

    def test_query_active_blocks(self):
        self.bm.load_block("testblock")
        self.assertEqual(self.bm.query_active_blocks("key1"), "value1")
        self.assertIsNone(self.bm.query_active_blocks("nonexistent"))

if __name__ == "__main__":
    unittest.main()
