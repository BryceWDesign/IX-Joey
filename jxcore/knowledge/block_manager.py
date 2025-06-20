# jxcore/knowledge/block_manager.py
"""
Knowledge Block Manager:
- Load/unload knowledge blocks dynamically
- Track active blocks
- Provide query interface to active knowledge
"""

import os
import json
from threading import RLock
from jxcore.utils.serialization import load_json_safe, save_json_safe

class BlockManager:
    def __init__(self, blocks_dir="knowledge_blocks"):
        self.blocks_dir = blocks_dir
        self.active_blocks = {}
        self.lock = RLock()

    def load_block(self, block_name):
        with self.lock:
            path = os.path.join(self.blocks_dir, f"{block_name}.json")
            block = load_json_safe(path)
            if block:
                self.active_blocks[block_name] = block
                return True
            return False

    def unload_block(self, block_name):
        with self.lock:
            if block_name in self.active_blocks:
                del self.active_blocks[block_name]
                return True
            return False

    def reload_block(self, block_name):
        with self.lock:
            self.unload_block(block_name)
            return self.load_block(block_name)

    def get_block(self, block_name):
        with self.lock:
            return self.active_blocks.get(block_name)

    def list_active_blocks(self):
        with self.lock:
            return list(self.active_blocks.keys())

    def query_active_blocks(self, query_key):
        """
        Search query_key across all active blocks, return first match or None.
        """
        with self.lock:
            for block_name, block in self.active_blocks.items():
                if query_key in block:
                    return block[query_key]
            return None

