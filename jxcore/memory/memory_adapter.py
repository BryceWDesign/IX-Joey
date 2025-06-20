# jxcore/memory/memory_adapter.py
"""
Memory Adapter:
- Extend session memory with active knowledge block tagging
- Allows tracking of which blocks influenced responses
"""

from jxcore.memory.session_tracker import MemoryTracker

class MemoryAdapter:
    def __init__(self, memory_tracker: MemoryTracker):
        self.memory_tracker = memory_tracker

    def add_session_with_context(self, input_text, triplet_data, response_text, active_blocks):
        session = {
            "session_id": self._generate_session_id(),
            "timestamp": self._current_timestamp(),
            "input": input_text,
            "triplet": triplet_data,
            "response": response_text,
            "active_blocks": active_blocks
        }
        self.memory_tracker.sessions.append(session)
        self.memory_tracker.save_memory()

    def _generate_session_id(self):
        import uuid
        return str(uuid.uuid4())

    def _current_timestamp(self):
        from datetime import datetime
        return datetime.utcnow().isoformat() + "Z"

