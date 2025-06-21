"""
IX-Joey Core Module

Handles natural language input processing, interpretation,
and communication with IX-Gibson for knowledge retrieval.
"""

from config.joey_config import MAX_INPUT_LENGTH, VERBOSE_OUTPUT
from utils.text_processing import normalize_text, tokenize
from core.gibson_adapter import GibsonAdapter

class JoeyCore:
    def __init__(self):
        self.gibson_adapter = GibsonAdapter()

    def interpret(self, user_input: str) -> str:
        """
        Process user input text, normalize and tokenize,
        then query IX-Gibson for a response.

        Args:
            user_input (str): Raw text input from user.

        Returns:
            str: Response text from IX-Gibson or error message.
        """
        if len(user_input) > MAX_INPUT_LENGTH:
            return "Input too long. Please shorten your query."

        normalized = normalize_text(user_input)
        tokens = tokenize(normalized)

        # For now, just join tokens and send to Gibson
        query_text = ' '.join(tokens)

        response = self.gibson_adapter.query_gibson(query_text)

        if VERBOSE_OUTPUT:
            print(f"[DEBUG] Query sent to Gibson: {query_text}")
            print(f"[DEBUG] Gibson response: {response}")

        if isinstance(response, dict) and "error" in response:
            return f"Error: {response['error']}"

        # Assuming response contains 'answer' field
        return response.get("answer", "No answer returned from Gibson.")
