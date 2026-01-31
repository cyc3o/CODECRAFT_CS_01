#!/usr/bin/env python3
"""
ADVANCED CAESAR CIPHER LAB
BRUTAL EDITION — SOC BUILD
Author : Vishal
Domain : SOC | Cryptanalysis | Forensics
Entry  : main.py (ONLY RUN THIS FILE)
"""

# =========================================================
# CORE IMPORTS
# =========================================================
from core.banner import banner
from core.auth import login
from core.menu import menu

from forensic.database import init_db
from utils.colors import GRAY, RESET


# =========================================================
# BOOT SEQUENCE
# =========================================================
def boot():
    """
    Full controlled startup sequence
    """
    banner()
    print(GRAY + "\n SYSTEM STATUS : INITIALIZING MODULES..." + RESET)
    init_db()
    input(GRAY + "\n PRESS ENTER TO CONTINUE >>> " + RESET)


# =========================================================
# MAIN EXECUTION FLOW
# =========================================================
def main():
    """
    Correct SOC execution order
    """
    boot()        # Banner + DB init
    login()       # Access control
    menu()        # Main SOC menu loop


# =========================================================
# ENTRY POINT (DO NOT TOUCH)
# =========================================================
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n SESSION TERMINATED BY USER")
    except Exception as e:
        print("\n\n CRITICAL ERROR :", str(e))