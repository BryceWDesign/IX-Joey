# jxcore/memory/session_tracker.py

import json
import uuid
from datetime import datetime
import os

class MemoryTracker:
    def __init__(self, memory_file="memstore.json"):
        self.memory_file = os.path.join(os.path.dirname(__file__), memory_file)
        self.sessions = self.load_memory()

    def load_memory(self):
        try:
            with open(self.memory_file, "r", encoding="utf-8") as f:
                data = json.load(f)
                return data.get("sessions", [])
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_memory(self):
        with open(self.memory_file, "w", encoding="utf-8") as f:
            json.dump({"sessions": self.sessions}, f, indent=4)

    def add_session(self, input_text, triplet_data, response_text):
        session = {
            "session_id": str(uuid.uuid4()),
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "input": input_text,
            "triplet": triplet_data,
            "response": response_text
        }
        self.sessions.append(session)
        self.save_memory()

    def recent_sessions(self, n=5):
        return self.sessions[-n:]

    def clear_memory(self):
        self.sessions = []
        self.save_memory()

    def find_by_input(self, query):
        return [s for s in self.sessions if query.lower() in s["input"].lower()]

    def print_memory(self):
        for i, s in enumerate(self.sessions):
            print(f"Session {i + 1}: {s['input']} → {s['response']}")
