# /joey/joey.py

import os
import sys
from alpha_core.grammar_root import GrammarEngine
from alpha_core.phonetic_decoder import PhoneticDecoder
from brain.semantic_mapper import SemanticMapper
from memory.thread_memory import ThreadMemory

class Joey:
    def __init__(self):
        self.grammar = GrammarEngine()
        self.phonetics = PhoneticDecoder()
        self.mapper = SemanticMapper()
        self.memory = ThreadMemory()
        self.session_log = []

        print("👶 IX-JOEY is awake. Teach me!")

    def interpret_input(self, user_input):
        # Phonetic analysis
        phonetic_form = self.phonetics.transcribe(user_input)

        # Grammar + syntax breakdown
        grammar_tags = self.grammar.parse(user_input)

        # Semantic interpretation
        meaning = self.mapper.interpret(grammar_tags)

        # Memory log
        self.memory.save_input(user_input, phonetic_form, grammar_tags, meaning)

        return {
            "phonetics": phonetic_form,
            "grammar": grammar_tags,
            "meaning": meaning
        }

    def chat(self):
        print("Type 'exit' to quit.")
        while True:
            user_input = input("\n👤 You: ").strip()
            if user_input.lower() == 'exit':
                print("👋 Bye-bye!")
                break

            result = self.interpret_input(user_input)

            print("\n🧠 Joey:")
            print(f"• Phonetics: {result['phonetics']}")
            print(f"• Grammar: {result['grammar']}")
            print(f"• Interpreted Meaning: {result['meaning']}")

            self.session_log.append((user_input, result))


if __name__ == "__main__":
    joey = Joey()
    joey.chat()
