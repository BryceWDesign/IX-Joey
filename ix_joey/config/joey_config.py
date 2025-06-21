"""
IX-Joey Configuration Module

Holds configurable parameters such as logging levels,
Gibson API connection details, and operational flags.
"""

import logging

# Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
LOG_LEVEL = logging.DEBUG

# Gibson API endpoint URL (override if needed)
GIBSON_API_URL = "http://localhost:9000/api/query"

# Maximum length of input text allowed
MAX_INPUT_LENGTH = 1024

# Enable verbose output for debugging
VERBOSE_OUTPUT = True
