"""
HELPER UTILITIES - SOC CORE
Author : Vishal
Purpose: Shared safe helpers for the entire project
Note   : ASCII ONLY (PYDROID SAFE)
"""

import hashlib
import sys
from utils.colors import GRAY, RED, RESET


# =========================================================
# HASHING (FORENSIC SAFE)
# =========================================================
def sha256(text):
    """
    Return SHA256 hash of input text
    """
    if not isinstance(text, str):
        text = str(text)
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


# =========================================================
# SAFE SHIFT INPUT
# =========================================================
def get_shift():
    """
    Get Caesar shift value safely (1-25)
    """
    try:
        value = input(GRAY + " SHIFT (1-25) >>> " + RESET)
        shift = int(value)

        if 1 <= shift <= 25:
            return shift

    except Exception:
        pass

    print(RED + " INVALID SHIFT VALUE" + RESET)
    return None


# =========================================================
# SAFE TEXT INPUT
# =========================================================
def get_text(prompt=" ENTER TEXT >>> "):
    """
    Safe wrapper for input()
    """
    try:
        return input(GRAY + prompt + RESET)
    except KeyboardInterrupt:
        print("\n" + RED + " INPUT CANCELLED BY USER" + RESET)
        return ""


# =========================================================
# BANNER LINE (NO UNICODE)
# =========================================================
def banner_line(char="-", size=50):
    """
    Print a clean separator line
    """
    try:
        print(GRAY + (char * size) + RESET)
    except Exception:
        print(char * size)


# =========================================================
# SAFE EXIT
# =========================================================
def safe_exit(message=" SESSION TERMINATED"):
    """
    Controlled program exit
    """
    print("\n" + RED + message + RESET)
    sys.exit(0)