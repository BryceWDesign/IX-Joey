# jxcore/config/knowledge_settings.py

import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

KNOWLEDGE_BLOCKS_DIR = os.path.join(BASE_DIR, "knowledge_blocks")

CONTEXT_MAP = {
    "medical": {
        "keywords": ["doctor", "medicine", "patient", "hospital"],
        "blocks": ["med_block"]
    },
    "mechanical": {
        "keywords": ["engine", "wrench", "machine", "repair"],
        "blocks": ["mech_block"]
    },
    "legal": {
        "keywords": ["law", "contract", "court", "judge"],
        "blocks": ["legal_block"]
    }
}

UPDATE_FREQUENCY_SECONDS = 3600  # hourly updates

CACHE_MAX_SIZE = 1000

DEBUG_MODE = True
