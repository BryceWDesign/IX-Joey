"""
Text Processing Utilities for IX-Joey

Functions to clean, normalize, and tokenize user input text
for better interpretation and Gibson compatibility.
"""

import re

def normalize_text(text: str) -> str:
    """
    Normalize input text by:
    - Lowercasing
    - Removing extra whitespace
    - Stripping unwanted characters

    Args:
        text (str): Raw input text.

    Returns:
        str: Normalized text.
    """
    text = text.lower()
    text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with single space
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation except whitespace
    return text.strip()

def tokenize(text: str) -> list[str]:
    """
    Tokenize normalized text into words.

    Args:
        text (str): Normalized input text.

    Returns:
        list[str]: List of word tokens.
    """
    return text.split()
