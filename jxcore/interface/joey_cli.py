# jxcore/interface/joey_cli.py

import json
import os
from jxcore.core_loop import JXCore
from jxcore.memory.session_tracker import MemoryTracker

def load_json(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

def main():
    # Load data files
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    root_map = load_json(os.path.join(base_path, "linguistics", "root_map.json"))
    morph_bank = load_json(os.path.join(base_path, "linguistics", "morph_bank.json"))
    semantic_patterns = load_json(os.path.join(base_path, "linguistics", "semantic_archetypes.json"))

    # Initialize Joey Core + Memory
    brain = JXCore(root_map, morph_bank, semantic_patterns)
    memory = MemoryTracker(memory_file=os.path.join(base_path, "memory", "memstore.json"))

    print("\n👋 Hello! I'm Joey. Let's talk. (type 'exit' to quit)")
    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() in ["exit", "quit"]:
            print("👋 Goodbye!")
            break

        parsed = brain.parse_input(user_input)
        pattern = brain.extract_pattern(parsed)
        reply = brain.respond(pattern)

        memory.add_session(user_input, pattern, reply)
        print("Joey:", reply)

if __name__ == "__main__":
    main()
