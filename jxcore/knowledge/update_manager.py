# jxcore/knowledge/update_manager.py
"""
Update Manager:
- Handle safe knowledge block updates without downtime
- Supports versioning and rollback
"""

import os
import shutil
from jxcore.knowledge.block_storage import BlockStorage

class UpdateManager:
    def __init__(self, storage: BlockStorage):
        self.storage = storage
        self.backup_dir = os.path.join(self.storage.blocks_dir, "_backups")
        os.makedirs(self.backup_dir, exist_ok=True)

    def backup_block(self, block_name):
        src = os.path.join(self.storage.blocks_dir, f"{block_name}.json")
        dst = os.path.join(self.backup_dir, f"{block_name}_{self._timestamp()}.json")
        if os.path.isfile(src):
            shutil.copy2(src, dst)
            return True
        return False

    def rollback_block(self, block_name, backup_filename):
        src = os.path.join(self.backup_dir, backup_filename)
        dst = os.path.join(self.storage.blocks_dir, f"{block_name}.json")
        if os.path.isfile(src):
            shutil.copy2(src, dst)
            return True
        return False

    def update_block(self, block_name, new_data):
        """
        Backup current, write new data, and confirm.
        """
        self.backup_block(block_name)
        return self.storage.save_block(block_name, new_data)

    def _timestamp(self):
        from datetime import datetime
        return datetime.utcnow().strftime("%Y%m%d%H%M%S")

