# jxcore/knowledge/block_storage.py
"""
Block Storage:
- Manage persistent storage of knowledge blocks
- Save/load/update block JSON files safely
"""

import os
from jxcore.utils.serialization import load_json_safe, save_json_safe

class BlockStorage:
    def __init__(self, blocks_dir="knowledge_blocks"):
        self.blocks_dir = blocks_dir
        os.makedirs(self.blocks_dir, exist_ok=True)

    def save_block(self, block_name, block_data):
        path = os.path.join(self.blocks_dir, f"{block_name}.json")
        return save_json_safe(path, block_data)

    def load_block(self, block_name):
        path = os.path.join(self.blocks_dir, f"{block_name}.json")
        return load_json_safe(path)

    def delete_block(self, block_name):
        path = os.path.join(self.blocks_dir, f"{block_name}.json")
        if os.path.isfile(path):
            os.remove(path)
            return True
        return False

    def list_blocks(self):
        return [f[:-5] for f in os.listdir(self.blocks_dir) if f.endswith(".json")]

