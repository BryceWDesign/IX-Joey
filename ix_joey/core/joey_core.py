"""
IX-Joey Core Module

Handles natural language understanding and generation,
integrating with IX-Gibson for advanced contextual knowledge.
"""

from .gibson_adapter import GibsonAdapter

class JoeyCore:
    def __init__(self):
        self.gibson = GibsonAdapter()

    def interpret(self, text: str) -> str:
        """
        Interpret user input text and generate a contextually
        appropriate response by querying IX-Gibson.

        Args:
            text (str): The input text to interpret.

        Returns:
            str: Response generated from IX-Gibson.
        """
        response = self.gibson.query_gibson(text)
        if "error" in response:
            return f"[Joey Error] {response['error']}"
        return response.get("answer", "[Joey] No answer available.")
