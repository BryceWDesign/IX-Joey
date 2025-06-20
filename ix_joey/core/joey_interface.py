"""
IX-Joey User Interface Module

Handles user interaction, forwards input to JoeyCore, and returns responses.
Updated to support the Gibson-aware JoeyCore for expert querying.
"""

from joey_core import JoeyCore

class JoeyInterface:
    def __init__(self):
        self.core = JoeyCore()

    def receive_input(self, user_text: str) -> str:
        """
        Receive user input, forward to core processing,
        and return the generated response.
        """
        response = self.core.process_input(user_text)
        return response

    def run(self):
        """
        Simple command line interface for demonstration.
        """
        print("IX-Joey is online. Type your questions.")
        while True:
            user_input = input("You: ")
            if user_input.strip().lower() in ['exit', 'quit']:
                print("IX-Joey shutting down. Goodbye!")
                break
            output = self.receive_input(user_input)
            print(f"Joey: {output}")
