# /alpha_core/grammar_root.py

import re

class GrammarEngine:
    def __init__(self):
        self.parts_of_speech = {
            'noun': ['dog', 'cat', 'apple', 'Joey', 'sky'],
            'verb': ['run', 'eat', 'is', 'am', 'are', 'jump'],
            'adjective': ['blue', 'fast', 'happy'],
            'adverb': ['quickly', 'silently'],
            'pronoun': ['I', 'you', 'he', 'she', 'it'],
            'preposition': ['in', 'on', 'under', 'over'],
            'conjunction': ['and', 'but', 'or'],
            'article': ['a', 'an', 'the']
        }

        self.grammar_rules = [
            'Subject Verb Object',
            'Article Adjective Noun',
            'Pronoun Verb Noun',
            'Noun Verb Adverb',
        ]

    def tokenize(self, sentence):
        return re.findall(r"\b\w+\b", sentence)

    def identify_part_of_speech(self, word):
        for pos, words in self.parts_of_speech.items():
            if word.lower() in [w.lower() for w in words]:
                return pos
        return 'unknown'

    def parse(self, sentence):
        tokens = self.tokenize(sentence)
        tagged = [(word, self.identify_part_of_speech(word)) for word in tokens]
        return tagged

    def explain(self, tagged_tokens):
        explanation = []
        for word, tag in tagged_tokens:
            explanation.append(f"{word} ➜ {tag}")
        return explanation

# Test (when running standalone)
if __name__ == "__main__":
    engine = GrammarEngine()
    sentence = "The blue dog runs quickly"
    tags = engine.parse(sentence)
    print("Tagged:", tags)
    print("Explanation:", engine.explain(tags))
