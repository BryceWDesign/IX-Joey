# /brain/semantic_mapper.py

class SemanticMapper:
    def __init__(self):
        self.last_structure = {}

    def interpret(self, tagged_tokens):
        structure = {
            "subject": None,
            "verb": None,
            "object": None,
            "modifiers": [],
            "unknowns": []
        }

        current = None

        for word, tag in tagged_tokens:
            tag = tag.lower()

            if tag in ["pronoun", "noun"] and not structure["subject"]:
                structure["subject"] = word
                current = "subject"
            elif tag == "verb" and not structure["verb"]:
                structure["verb"] = word
                current = "verb"
            elif tag in ["noun", "pronoun"] and structure["subject"] and structure["verb"] and not structure["object"]:
                structure["object"] = word
                current = "object"
            elif tag in ["adjective", "adverb", "article", "preposition", "conjunction"]:
                structure["modifiers"].append((word, tag))
            else:
                structure["unknowns"].append((word, tag))

        self.last_structure = structure
        return structure

    def summarize(self):
        """Simple natural language summary of last parsed input"""
        s = self.last_structure.get("subject", "Someone")
        v = self.last_structure.get("verb", "did something")
        o = self.last_structure.get("object", "")
        if o:
            return f"{s} {v} {o}."
        else:
            return f"{s} {v}."

# Test Mode
if __name__ == "__main__":
    mapper = SemanticMapper()
    tagged = [("The", "article"), ("blue", "adjective"), ("dog", "noun"), ("runs", "verb"), ("quickly", "adverb")]
    result = mapper.interpret(tagged)
    print("Structure:", result)
    print("Summary:", mapper.summarize())
