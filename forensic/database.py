"""
DATABASE ENGINE — FORENSIC CORE
Author : Vishal
Domain : SOC | Forensics | Audit Logging
DB     : SQLite (Local, Portable)
"""

import sqlite3
import os
from datetime import datetime
from utils.colors import GRAY, ORANGE, RESET

# =========================================================
# DATABASE CONFIG
# =========================================================
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
DB_PATH  = os.path.join(DATA_DIR, "caesar_lab.db")


# =========================================================
# DATABASE INITIALIZATION
# =========================================================
def init_db():
    """
    Initializes forensic database safely
    """
    os.makedirs(DATA_DIR, exist_ok=True)

    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS LOGS (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            ACTION TEXT NOT NULL,
            SHIFT INTEGER,
            INPUT_HASH TEXT,
            OUTPUT_HASH TEXT,
            TIMESTAMP TEXT
        )
    """)

    con.commit()
    con.close()

    print(ORANGE + " DATABASE STATUS : READY" + RESET)


# =========================================================
# DATABASE CONNECTION (REUSABLE)
# =========================================================
def db_connect():
    """
    Returns a database connection
    """
    return sqlite3.connect(DB_PATH)


# =========================================================
# FORENSIC READ (LATEST LOGS)
# =========================================================
def fetch_logs(limit=10):
    """
    Fetch recent forensic logs
    """
    con = db_connect()
    cur = con.cursor()

    cur.execute("""
        SELECT ACTION, SHIFT, TIMESTAMP
        FROM LOGS
        ORDER BY ID DESC
        LIMIT ?
    """, (limit,))

    rows = cur.fetchall()
    con.close()
    return rows


# =========================================================
# DATABASE HEALTH CHECK
# =========================================================
def db_status():
    """
    Simple DB health check
    """
    if os.path.exists(DB_PATH):
        print(GRAY + f" DB PATH : {DB_PATH}" + RESET)
        print(GRAY + " DB STATE: ACTIVE" + RESET)
    else:
        print(GRAY + " DB STATE: NOT FOUND" + RESET)