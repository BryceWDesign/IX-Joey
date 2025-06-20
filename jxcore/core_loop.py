# jxcore/core_loop.py

class JXCore:
    def __init__(self, root_map, morph_bank, semantic_patterns):
        """
        root_map: word → root form (lemmatizer/morph reducer)
        morph_bank: root form → {"meaning": ..., "type": ...}
        semantic_patterns: core logic templates for sentence modeling
        """
        self.root_map = root_map
        self.morph_bank = morph_bank
        self.semantic_patterns = semantic_patterns

    def parse_input(self, sentence):
        """
        Step 1: Tokenize and map each word to its root and type.
        """
        words = sentence.lower().split()
        parsed = []

        for word in words:
            root = self.root_map.get(word, word)
            morph = self.morph_bank.get(root, {"meaning": "unknown", "type": "unknown"})
            parsed.append({
                "word": word,
                "root": root,
                "type": morph["type"],
                "meaning": morph["meaning"]
            })

        return parsed

    def extract_pattern(self, parsed):
        """
        Step 2: Create a symbolic action structure (who → does → what → modifiers).
        """
        pattern = {
            "who": None,
            "does": None,
            "what": None,
            "modifiers": []
        }

        for token in parsed:
            kind = token["type"]
            word = token["word"]
            if kind == "noun" and not pattern["who"]:
                pattern["who"] = word
            elif kind == "verb" and not pattern["does"]:
                pattern["does"] = word
            elif kind == "noun" and pattern["who"] and pattern["does"] and not pattern["what"]:
                pattern["what"] = word
            elif kind in ["adjective", "adverb"]:
                pattern["modifiers"].append(word)

        return pattern

    def respond(self, pattern):
        """
        Step 3: Generate an interpreted response from symbolic structure.
        """
        who = pattern.get("who") or "Someone"
        does = pattern.get("does") or "does something"
        what = pattern.get("what") or ""
        mods = " ".join(pattern.get("modifiers", []))

        return f"{who} {does} {what} {mods}".strip()

    def think(self, sentence):
        """
        Entire process: Input → Parse → Extract → Respond
        """
        parsed = self.parse_input(sentence)
        pattern = self.extract_pattern(parsed)
        response = self.respond(pattern)
        return response

# Demo usage
if __name__ == "__main__":
    root_map = {
        "ran": "run", "runs": "run", "running": "run",
        "dogs": "dog", "quickly": "quick", "happily": "happy",
        "ate": "eat", "eats": "eat", "eating": "eat"
    }

    morph_bank = {
        "run": {"meaning": "move fast on foot", "type": "verb"},
        "dog": {"meaning": "domesticated animal", "type": "noun"},
        "quick": {"meaning": "high speed", "type": "adverb"},
        "happy": {"meaning": "joyful", "type": "adverb"},
        "eat": {"meaning": "consume food", "type": "verb"},
        "cat": {"meaning": "feline animal", "type": "noun"},
        "apple": {"meaning": "edible fruit", "type": "noun"}
    }

    semantic_patterns = {}  # Will be used in advanced versions

    brain = JXCore(root_map, morph_bank, semantic_patterns)

    test_sentences = [
        "The dog ran quickly",
        "A cat eats an apple",
        "She happily runs"
    ]

    for sent in test_sentences:
        print(f"Input: {sent}")
        print("Output:", brain.think(sent))
        print("---")
