"""
CASE REPORT GENERATOR — SOC
Author : Vishal
Domain : SOC | Incident Response | Forensics
"""

import os
from datetime import datetime
from forensic.database import db_connect
from utils.colors import ORANGE, WHITE, GRAY, SUCCESS, RESET
from utils.helpers import banner_line


# =========================================================
# REPORT CONFIG
# =========================================================
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
REPORT_DIR = os.path.join(BASE_DIR, "reports")
REPORT_FILE = os.path.join(REPORT_DIR, "CASE_REPORT.txt")


# =========================================================
# EXPORT SOC CASE REPORT
# =========================================================
def export_report():
    """
    Generate forensic SOC case report
    """
    os.makedirs(REPORT_DIR, exist_ok=True)

    con = db_connect()
    cur = con.cursor()

    cur.execute("""
        SELECT ACTION, SHIFT, TIMESTAMP
        FROM LOGS
        ORDER BY ID DESC
    """)

    rows = cur.fetchall()
    con.close()

    with open(REPORT_FILE, "w", encoding="utf-8") as f:
        f.write("ADVANCED CAESAR CIPHER LAB — SOC CASE REPORT\n")
        f.write("=" * 55 + "\n\n")
        f.write(f"Generated (UTC) : {datetime.utcnow().isoformat()}\n")
        f.write("Analyst         : Vishal\n")
        f.write("Classification  : INTERNAL / TRAINING\n\n")

        if not rows:
            f.write("No forensic events recorded.\n")
        else:
            f.write("FORENSIC EVENT LOG\n")
            f.write("-" * 40 + "\n")
            for i, (action, shift, ts) in enumerate(rows, 1):
                f.write(f"{i}. {action} | SHIFT {shift} | {ts}\n")

    print(ORANGE + "\n SOC CASE REPORT GENERATED" + RESET)
    print(SUCCESS + f" FILE : {REPORT_FILE}" + RESET)
    banner_line()