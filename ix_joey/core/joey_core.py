"""
IX-Joey Core Reasoning Module with Gibson Integration

This module implements the core logic of IX-Joey, now enhanced to communicate with IX-Gibson
using the GibsonAdapter. This enables Joey to send domain-specific queries and receive
specialized expert responses in real-time.
"""

from gibson_adapter import GibsonAdapter

class JoeyCore:
    def __init__(self):
        self.gibson = GibsonAdapter()
        self.active_context = {}

    def process_input(self, user_input: str) -> str:
        """
        Main input processing method.
        Parses user input to detect if a Gibson domain query is requested.
        If yes, delegates to Gibson and returns expert answer.
        Otherwise, uses internal logic (placeholder here).
        """
        domain, question = self._parse_gibson_query(user_input)
        if domain and question:
            answer = self.gibson.send_query(domain, question)
            return f"[Gibson Expert Answer] {answer}"
        else:
            # Placeholder for Joey's own reasoning / fallback
            return self._default_response(user_input)

    def _parse_gibson_query(self, text: str):
        """
        Simple heuristic parser to extract domain and question for Gibson.
        Format expected: "Ask <domain>: <question>"
        e.g. "Ask biology: what is the function of mitochondria?"
        """
        prefix = "ask "
        text_lower = text.lower()
        if text_lower.startswith(prefix):
            try:
                # Example input: "ask physics: what is gravity?"
                remainder = text_lower[len(prefix):].strip()
                domain, question = remainder.split(":", 1)
                return domain.strip(), question.strip()
            except ValueError:
                return None, None
        return None, None

    def _default_response(self, text: str) -> str:
        """
        Placeholder for Joey's fallback response logic.
        """
        return f"I am Joey, but I don't understand your question: {text}"

