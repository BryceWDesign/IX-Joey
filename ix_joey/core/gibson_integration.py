"""
IX-Joey Gibson Integration Core

This module centralizes all communication and integration logic
between IX-Joey and IX-Gibson. It handles requests, responses,
error processing, and acts as a liaison to the Gibson utility functions.
"""

from utils.gibson_comm import send_gibson_request

class GibsonIntegration:
    def __init__(self):
        pass

    def query_gibson(self, domain: str, question: str) -> str:
        """
        Send a query to IX-Gibson and process the response.

        Args:
            domain (str): Domain expertise requested (e.g., biology, physics).
            question (str): The user's question.

        Returns:
            str: Formatted answer or error message.
        """
        payload = {
            "domain": domain,
            "question": question,
            "from": "ix-joey"
        }
        response = send_gibson_request(payload)
        if "error" in response:
            return f"[Gibson Error]: {response['error']}"
        return response.get("answer", "[Gibson]: No answer provided.")
