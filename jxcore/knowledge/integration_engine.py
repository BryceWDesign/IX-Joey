# jxcore/knowledge/integration_engine.py
"""
Integration Engine:
- Combine and harmonize knowledge from multiple active blocks
- Resolve conflicts and merge reasoning results
"""

class IntegrationEngine:
    def __init__(self, block_manager):
        self.block_manager = block_manager

    def query(self, query_key):
        """
        Query all active blocks and merge results intelligently.
        """
        matches = []
        for block_name in self.block_manager.list_active_blocks():
            block = self.block_manager.get_block(block_name)
            if not block:
                continue
            if query_key in block:
                matches.append((block_name, block[query_key]))

        # Simple merge: if multiple results, prefer first or merge list if possible
        if not matches:
            return None
        if len(matches) == 1:
            return matches[0][1]

        # Example merge logic (override with project-specific merge rules)
        merged = []
        for _, data in matches:
            if isinstance(data, list):
                merged.extend(data)
            else:
                merged.append(data)
        # Deduplicate merged list
        return list(set(merged))

