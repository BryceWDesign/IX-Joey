# jxcore/interface/joey_cli.py

import json
import os
from jxcore.core_loop import JXCore
from jxcore.memory.session_tracker import MemoryTracker
from jxcore.knowledge.block_manager import BlockManager
from jxcore.knowledge.context_switcher import ContextSwitcher
from jxcore.memory.memory_adapter import MemoryAdapter
from jxcore.config.knowledge_settings import CONTEXT_MAP

def load_json(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

def main():
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    root_map = load_json(os.path.join(base_path, "linguistics", "root_map.json"))
    morph_bank = load_json(os.path.join(base_path, "linguistics", "morph_bank.json"))
    semantic_patterns = load_json(os.path.join(base_path, "linguistics", "semantic_archetypes.json"))

    brain = JXCore(root_map, morph_bank, semantic_patterns)
    memory = MemoryTracker(memory_file=os.path.join(base_path, "memory", "memstore.json"))
    memory_adapter = MemoryAdapter(memory)
    block_manager = BlockManager(os.path.join(base_path, "knowledge_blocks"))
    context_switcher = ContextSwitcher(block_manager, CONTEXT_MAP)

    print("\n👋 Hello! I'm Joey with modular knowledge! Type 'exit' to quit.")
    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() in ["exit", "quit"]:
            print("👋 Goodbye!")
            break

        context = context_switcher.switch_context(user_input)
        parsed = brain.parse_input(user_input)
        pattern = brain.extract_pattern(parsed)
        # Query knowledge blocks for enrichment
        knowledge_data = block_manager.query_active_blocks(pattern.get("does") or "")
        reply = brain.respond(pattern)
        if knowledge_data:
            reply += f" (Info from '{context}': {knowledge_data})"

        memory_adapter.add_session_with_context(user_input, pattern, reply, block_manager.list_active_blocks())
        print("Joey:", reply)

if __name__ == "__main__":
    main()
