"""
IX-Joey: Gibson Adapter Module

This module enables Joey to send structured knowledge queries to IX-Gibson and receive
expert responses routed through the hub. Only Joey has permission to initiate requests.
"""

import requests
import json

class GibsonAdapter:
    def __init__(self, gibson_url="http://localhost:8492/gibson"):
        self.gibson_url = gibson_url

    def send_query(self, domain: str, question: str) -> str:
        payload = {
            "domain": domain,
            "question": question,
            "from": "ix-joey"
        }
        try:
            response = requests.post(self.gibson_url, json=payload, timeout=10)
            if response.status_code == 200:
                return response.json().get("answer", "[Gibson]: No response.")
            else:
                return f"[Gibson ERROR {response.status_code}]: {response.text}"
        except Exception as e:
            return f"[Gibson COMM ERROR]: {str(e)}"
