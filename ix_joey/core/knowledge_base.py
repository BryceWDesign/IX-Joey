"""
IX-Joey Knowledge Base Module

Manages static and dynamic knowledge entries for IX-Joey.
Designed to be easily extendable for future advanced storage or retrieval.
"""

class KnowledgeBase:
    def __init__(self):
        self.static_knowledge = {
            "hello": "Hello! I am IX-Joey, your friendly AI assistant.",
            "weather": "I don't have live weather data yet, but I can help with other questions.",
            "who are you": "I am IX-Joey, a generalist AI sibling designed to assist you.",
        }
        self.dynamic_knowledge = {}

    def get_answer(self, query: str) -> str:
        query_lower = query.lower()
        # Check dynamic knowledge first
        if query_lower in self.dynamic_knowledge:
            return self.dynamic_knowledge[query_lower]
        # Check static knowledge next
        for key in self.static_knowledge:
            if key in query_lower:
                return self.static_knowledge[key]
        return "I'm still learning! Could you please rephrase or ask another question?"

    def add_dynamic_knowledge(self, key: str, value: str):
        self.dynamic_knowledge[key.lower()] = value

# Simple test
if __name__ == "__main__":
    kb = KnowledgeBase()
    print(kb.get_answer("Hello there!"))
    kb.add_dynamic_knowledge("AI", "Artificial Intelligence is the simulation of human intelligence.")
    print(kb.get_answer("What is AI?"))
