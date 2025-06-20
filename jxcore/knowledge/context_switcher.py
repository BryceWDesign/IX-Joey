# jxcore/knowledge/context_switcher.py
"""
Context Switcher:
- Detect context/task changes in input
- Activate/deactivate knowledge blocks accordingly
"""

import re
from jxcore.knowledge.block_manager import BlockManager

class ContextSwitcher:
    def __init__(self, block_manager: BlockManager, context_map=None):
        self.block_manager = block_manager
        self.context_map = context_map or {}  # e.g. {'medical': ['med_block'], 'mechanical': ['mech_block']}

        self.current_context = None

    def detect_context(self, user_input):
        """
        Basic keyword matching to detect context.
        More sophisticated NLP can replace this.
        """
        for ctx, keywords in self.context_map.items():
            for kw in keywords.get("keywords", []):
                if re.search(rf"\b{kw}\b", user_input, flags=re.I):
                    return ctx
        return None

    def switch_context(self, user_input):
        new_context = self.detect_context(user_input)
        if new_context != self.current_context:
            # Deactivate old blocks
            if self.current_context:
                for block in self.context_map[self.current_context].get("blocks", []):
                    self.block_manager.unload_block(block)

            # Activate new blocks
            if new_context:
                for block in self.context_map[new_context].get("blocks", []):
                    self.block_manager.load_block(block)

            self.current_context = new_context
            return new_context
        return self.current_context

