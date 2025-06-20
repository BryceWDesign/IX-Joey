# jxcore/utils/json_tools.py

import json
from typing import Any

def load_json_safe(filepath: str) -> Any:
    """
    Load JSON data from a file safely.
    Returns parsed JSON object or None on failure.
    """
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return None

def save_json_safe(filepath: str, data: Any) -> bool:
    """
    Save JSON data to a file safely.
    Returns True if successful, False otherwise.
    """
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        return True
    except Exception:
        return False

def validate_json_structure(data: Any, required_keys: list) -> bool:
    """
    Check if JSON object has all required keys.
    Returns True if valid, False if any key missing.
    """
    if not isinstance(data, dict):
        return False
    return all(key in data for key in required_keys)
