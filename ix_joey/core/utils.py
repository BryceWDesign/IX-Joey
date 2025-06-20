"""
IX-Joey Utilities Module

Provides helper functions for IX-Joey's core operations.
"""

import re

def clean_query(query: str) -> str:
    """
    Cleans input query by removing extra whitespace and special characters.
    """
    query = query.strip()
    # Remove excessive whitespace
    query = re.sub(r'\s+', ' ', query)
    return query

def is_valid_query(query: str) -> bool:
    """
    Basic validation to check if query is meaningful.
    """
    return bool(query and len(query) > 2)

# Example usage
if __name__ == "__main__":
    test_queries = [
        "   Hello!   ",
        "???!",
        "",
        "What is AI?"
    ]
    for q in test_queries:
        print(f"'{q}' -> Cleaned: '{clean_query(q)}', Valid: {is_valid_query(q)}")
