"""
MAIN MENU - SOC CONTROL PANEL
Author : Vishal
Domain : SOC | Cryptanalysis | Forensics
Mode   : ANALYST ASSIST (NON DETERMINISTIC)
"""

import secrets

from crypto.caesar import Caesar
from crypto.analysis import frequency_analysis, auto_crack

from forensic.database import init_db
from forensic.logger import log_event, view_logs
from forensic.reports import export_report

from security.threat_model import threat_model

from utils.colors import ORANGE, WHITE, GRAY, RED, RESET
from utils.helpers import get_shift, get_text, banner_line


# =========================================================
# MAIN MENU LOOP
# =========================================================
def menu():
    init_db()

    while True:
        print(ORANGE + "\n SOC ANALYST CONSOLE" + RESET)
        banner_line()

        print(WHITE + "[1] ENCRYPT TEXT (ANALYST INPUT)")
        print(WHITE + "[2] DECRYPT TEXT (ASSISTED)")
        print(WHITE + "[3] AUTO CRACK (RANKED RESULTS)")
        print(WHITE + "[4] RANDOM KEY ENCRYPT (DEMONSTRATION)")
        print(WHITE + "[5] FREQUENCY ANALYSIS (INTERPRETIVE)")
        print(WHITE + "[6] THREAT MODEL (CONTEXT VIEW)")
        print(WHITE + "[7] FORENSIC EVENT REVIEW")
        print(WHITE + "[8] EXPORT CASE REPORT")
        print(WHITE + "[0] EXIT")

        banner_line()

        ch = input(GRAY + " SELECT >> " + RESET).strip()

        # EXIT
        if ch == "0":
            print(RED + "\n SESSION TERMINATED BY ANALYST\n" + RESET)
            break

        # ENCRYPT
        elif ch == "1":
            text = get_text()
            shift = get_shift()
            if shift is None:
                continue

            result = Caesar(shift).enc(text)
            print(WHITE + " OUTPUT (NOT FINAL) : " + result.upper() + RESET)
            print(GRAY + " NOTE: OUTPUT IS DETERMINISTIC AND REVERSIBLE" + RESET)
            log_event("ENC", shift, text, result)

        # DECRYPT
        elif ch == "2":
            text = get_text()
            shift = get_shift()
            if shift is None:
                continue

            result = Caesar(shift).dec(text)
            print(WHITE + " OUTPUT (NOT VERIFIED) : " + result.upper() + RESET)
            print(GRAY + " NOTE: DECRYPTION ASSUMES CORRECT SHIFT" + RESET)
            log_event("DEC", shift, text, result)

        # AUTO CRACK
        elif ch == "3":
            cipher = get_text(" ENTER ENCRYPTED TEXT >>> ")
            print(GRAY + "\n ANALYST NOTICE:")
            print(GRAY + " TOOL PRESENTS RANKED POSSIBILITIES")
            print(GRAY + " FINAL INTERPRETATION IS USER RESPONSIBILITY\n" + RESET)
            auto_crack(cipher)

        # RANDOM KEY ENCRYPT
        elif ch == "4":
            text = get_text()
            shift = secrets.randbelow(25) + 1
            result = Caesar(shift).enc(text)
            print(WHITE + " OUTPUT (DEMO MODE) : " + result.upper() + RESET)
            print(GRAY + " KEY USED : " + str(shift) + RESET)
            print(GRAY + " NOTE: RANDOMIZATION DOES NOT IMPLY SECURITY" + RESET)
            log_event("ENC_RANDOM", shift, text, result)

        # FREQUENCY ANALYSIS
        elif ch == "5":
            text = get_text()
            print(GRAY + "\n ANALYST NOTICE:")
            print(GRAY + " FREQUENCY RESULTS REQUIRE CORRELATION")
            print(GRAY + " WITH BRUTE FORCE AND CONTEXTUAL ANALYSIS\n" + RESET)
            frequency_analysis(text)

        # THREAT MODEL
        elif ch == "6":
            threat_model()
            print(GRAY + "\n ANALYST NOTE:")
            print(GRAY + " THREAT MODEL DESCRIBES RISK NOT EXPLOITABILITY\n" + RESET)

        # LOG REVIEW
        elif ch == "7":
            view_logs()
            print(GRAY + "\n NOTE:")
            print(GRAY + " LOGS REPRESENT ACTION HISTORY NOT CONCLUSIONS\n" + RESET)

        # EXPORT REPORT
        elif ch == "8":
            export_report()
            print(GRAY + " REPORT IS A SNAPSHOT NOT FINAL JUDGMENT\n" + RESET)

        else:
            print(RED + " INVALID OPTION - ANALYST INPUT REQUIRED" + RESET)