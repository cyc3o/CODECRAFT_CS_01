"""
COLOR ENGINE — SOC / HACKER THEME
Author : Vishal
Safe   : Termux | Pydroid | Linux | Android
Style  : Brown + Shaddy Red (Unique Hacker Theme)
"""

# =========================================================
# ANDROID SAFE COLOR ENGINE
# =========================================================
try:
    from colorama import init
    init(autoreset=True)

    # ─── PRIMARY HACKER PALETTE ──────────────────────────
    BROWN   = "\033[38;5;94m"    # Main hacker brown
    RED     = "\033[38;5;124m"   # Deep blood red
    ORANGE  = "\033[38;5;166m"   # Warning / highlight
    GRAY    = "\033[38;5;245m"   # Muted system text
    WHITE   = "\033[97m"         # Clean output
    RESET   = "\033[0m"

    # ─── SPECIAL EFFECTS ─────────────────────────────────
    BOLD    = "\033[1m"
    DIM     = "\033[2m"
    UNDER   = "\033[4m"

    # ─── SOC STATUS COLORS ───────────────────────────────
    SUCCESS = "\033[38;5;34m"    # Green success
    FAIL    = RED                # Alias
    INFO    = ORANGE
    SYSTEM  = GRAY

except Exception:
    # ─── FALLBACK (NO COLOR SUPPORT) ─────────────────────
    BROWN = RED = ORANGE = GRAY = WHITE = RESET = ""
    BOLD = DIM = UNDER = ""
    SUCCESS = FAIL = INFO = SYSTEM = ""

# =========================================================
# UTILITY HELPERS (OPTIONAL)
# =========================================================
def cprint(color, text):
    """
    Safe colored print
    """
    print(f"{color}{text}{RESET}")