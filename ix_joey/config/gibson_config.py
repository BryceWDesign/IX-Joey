"""
IX-Joey Gibson Configuration

This configuration file centralizes parameters required to connect and
communicate with IX-Gibson, such as endpoint URLs and timeouts.
"""

GIBSON_API_URL = "http://localhost:8492/gibson"
REQUEST_TIMEOUT_SECONDS = 10
RETRY_ATTEMPTS = 3
RETRY_BACKOFF_SECONDS = 2
