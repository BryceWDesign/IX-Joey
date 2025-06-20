# jxcore/config/settings.py

import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

DATA_DIR = os.path.join(BASE_DIR, "jxcore", "data")
LINGUISTICS_DIR = os.path.join(BASE_DIR, "jxcore", "linguistics")
MEMORY_DIR = os.path.join(BASE_DIR, "jxcore", "memory")

ROOT_MAP_FILE = os.path.join(LINGUISTICS_DIR, "root_map.json")
MORPH_BANK_FILE = os.path.join(LINGUISTICS_DIR, "morph_bank.json")
SEMANTIC_ARCHETYPES_FILE = os.path.join(LINGUISTICS_DIR, "semantic_archetypes.json")

MEMORY_STORE_FILE = os.path.join(MEMORY_DIR, "memstore.json")

DEBUG_MODE = True

def debug_log(message: str):
    if DEBUG_MODE:
        print(f"[DEBUG] {message}")
