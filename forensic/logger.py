"""
FORENSIC LOGGER - SOC CORE
Author : Vishal
Purpose: Forensic event logging (analysis assist)
"""

from datetime import datetime
from forensic.database import db_connect
from utils.helpers import sha256
from utils.colors import ORANGE, GRAY, RESET


# =========================================================
# LOG EVENT
# =========================================================
def log_event(action, shift, input_text, output_text):
    con = db_connect()
    cur = con.cursor()

    cur.execute(
        "INSERT INTO LOGS (ACTION, SHIFT, INPUT_HASH, OUTPUT_HASH, TIMESTAMP) "
        "VALUES (?, ?, ?, ?, ?)",
        (
            action,
            shift,
            sha256(input_text),
            sha256(output_text),
            datetime.utcnow().isoformat()
        )
    )

    con.commit()
    con.close()


# =========================================================
# VIEW LOGS
# =========================================================
def view_logs(limit=10):
    con = db_connect()
    cur = con.cursor()

    cur.execute(
        "SELECT ACTION, SHIFT, TIMESTAMP FROM LOGS "
        "ORDER BY ID DESC LIMIT ?",
        (limit,)
    )

    rows = cur.fetchall()
    con.close()

    print(ORANGE + "\n FORENSIC EVENT REVIEW" + RESET)
    print(GRAY + " EVENTS REPRESENT ACTIONS, NOT CONCLUSIONS" + RESET)

    if not rows:
        print(GRAY + " NO EVENTS FOUND" + RESET)
        return

    index = 1
    for action, shift, ts in rows:
        print(
            GRAY +
            str(index) + ". EVENT=" + action +
            " | SHIFT=" + str(shift) +
            " | TIME=" + ts +
            RESET
        )
        index += 1