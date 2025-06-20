"""
Gibson Adapter — IX-Joey

Handles API communication between IX-Joey and IX-Gibson
central intelligence node.
"""

import requests
from ix_gibson.config.gibson_config import GIBSON_API_URL, REQUEST_TIMEOUT_SECONDS, RETRY_ATTEMPTS, RETRY_BACKOFF_SECONDS
import time

class GibsonAdapter:
    def __init__(self):
        self.api_url = GIBSON_API_URL
        self.timeout = REQUEST_TIMEOUT_SECONDS
        self.retries = RETRY_ATTEMPTS
        self.backoff = RETRY_BACKOFF_SECONDS

    def query_gibson(self, query_text: str) -> dict:
        """
        Sends a query to IX-Gibson and returns the response.

        Args:
            query_text (str): Text query to send.

        Returns:
            dict: Response data from IX-Gibson API.
        """
        for attempt in range(self.retries):
            try:
                response = requests.post(self.api_url, json={"query": query_text}, timeout=self.timeout)
                response.raise_for_status()
                return response.json()
            except requests.RequestException as e:
                time.sleep(self.backoff)
        return {"error": "Failed to communicate with IX-Gibson after retries."}
