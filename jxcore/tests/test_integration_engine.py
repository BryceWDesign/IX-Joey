# jxcore/tests/test_integration_engine.py

import unittest
from jxcore.knowledge.block_manager import BlockManager
from jxcore.knowledge.integration_engine import IntegrationEngine

class DummyBlockManager(BlockManager):
    def __init__(self):
        self.active_blocks = {
            "block1": {"key1": "value1", "list_key": [1, 2]},
            "block2": {"key1": "value2", "list_key": [2, 3]}
        }

    def list_active_blocks(self):
        return list(self.active_blocks.keys())

    def get_block(self, block_name):
        return self.active_blocks.get(block_name)

class TestIntegrationEngine(unittest.TestCase):
    def setUp(self):
        self.bm = DummyBlockManager()
        self.engine = IntegrationEngine(self.bm)

    def test_query_single_match(self):
        result = self.engine.query("key1")
        # Could be value1 or value2 depending on order, both acceptable
        self.assertIn(result, ["value1", "value2"])

    def test_query_merge_lists(self):
        result = self.engine.query("list_key")
        self.assertIsInstance(result, list)
        self.assertIn(1, result)
        self.assertIn(2, result)
        self.assertIn(3, result)

    def test_query_no_match(self):
        result = self.engine.query("nonexistent")
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()
