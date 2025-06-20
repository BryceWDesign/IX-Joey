"""
Utility module for IX-Joey to communicate reliably with IX-Gibson.

Includes retry logic, error handling, and response validation to ensure
stable interaction between IX-Joey and IX-Gibson services.
"""

import requests
import time
from config.gibson_config import GIBSON_API_URL, REQUEST_TIMEOUT_SECONDS, RETRY_ATTEMPTS, RETRY_BACKOFF_SECONDS

def send_gibson_request(payload: dict) -> dict:
    """
    Sends a POST request to the IX-Gibson API endpoint with retries.

    Args:
        payload (dict): The JSON payload to send.

    Returns:
        dict: Parsed JSON response from Gibson or an error dict.
    """
    for attempt in range(1, RETRY_ATTEMPTS + 1):
        try:
            response = requests.post(GIBSON_API_URL, json=payload, timeout=REQUEST_TIMEOUT_SECONDS)
            if response.status_code == 200:
                return response.json()
            else:
                # Non-200 response, log and retry
                print(f"Gibson returned HTTP {response.status_code}: {response.text}")
        except requests.RequestException as e:
            print(f"Gibson request error on attempt {attempt}: {e}")

        if attempt < RETRY_ATTEMPTS:
            time.sleep(RETRY_BACKOFF_SECONDS)

    return {"error": "Failed to communicate with IX-Gibson after multiple attempts."}
