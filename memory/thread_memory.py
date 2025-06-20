# /memory/thread_memory.py

import json
import os
from datetime import datetime

class ThreadMemory:
    def __init__(self, memory_file='joey_memory.json'):
        self.memory_file = memory_file
        self.memory_data = []

        if os.path.exists(self.memory_file):
            try:
                with open(self.memory_file, 'r', encoding='utf-8') as f:
                    self.memory_data = json.load(f)
            except Exception as e:
                print(f"[Memory Load Error] {e}")
                self.memory_data = []
        else:
            self._save()  # initialize file

    def save_input(self, input_text, phonetics, grammar_tags, semantics):
        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "input": input_text,
            "phonetics": phonetics,
            "grammar_tags": grammar_tags,
            "semantics": semantics
        }
        self.memory_data.append(entry)
        self._save()

    def _save(self):
        try:
            with open(self.memory_file, 'w', encoding='utf-8') as f:
                json.dump(self.memory_data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"[Memory Save Error] {e}")

    def get_last(self, n=1):
        return self.memory_data[-n:] if self.memory_data else []

    def search_inputs(self, keyword):
        return [entry for entry in self.memory_data if keyword.lower() in entry["input"].lower()]

    def clear_memory(self):
        self.memory_data = []
        self._save()

# Test Mode
if __name__ == "__main__":
    mem = ThreadMemory()
    mem.save_input(
        "The dog ran quickly",
        [('the', ['<UNK>']), ('dog', ['D', 'AO', 'G']), ('ran', ['<UNK>']), ('quickly', ['K', 'W', 'IH', 'K', 'L', 'IY'])],
        [('the', 'article'), ('dog', 'noun'), ('ran', 'verb'), ('quickly', 'adverb')],
        {"subject": "dog", "verb": "ran", "object": None, "modifiers": [("the", "article"), ("quickly", "adverb")], "unknowns": []}
    )

    print("Last Entry:", mem.get_last(1))
