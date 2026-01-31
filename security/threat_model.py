"""
THREAT MODEL — CAESAR CIPHER
Author : Vishal
Domain : SOC | Cryptanalysis | Risk Assessment
"""

from utils.colors import (
    RED, ORANGE, GRAY, WHITE, BROWN,
    SUCCESS, RESET
)
from utils.helpers import banner_line


# =========================================================
# THREAT MODEL OUTPUT
# =========================================================
def threat_model():
    banner_line()

    print(BROWN + " THREAT MODEL : CAESAR CIPHER" + RESET)
    print(GRAY  + " SOC ANALYSIS | CRYPTOGRAPHIC RISK" + RESET)
    banner_line()

    print(WHITE + " ATTACK VECTORS" + RESET)
    print(ORANGE + "  ▸ Brute Force (26 possible keys)")
    print(ORANGE + "  ▸ Frequency Analysis")
    print(ORANGE + "  ▸ Known Plaintext Attack")
    print(ORANGE + "  ▸ Dictionary-Based Guessing\n")

    print(WHITE + " IMPACT ASSESSMENT" + RESET)
    print(RED   + "  ▸ Confidentiality : FAILED")
    print(RED   + "  ▸ Integrity       : FAILED")
    print(RED   + "  ▸ Authenticity    : FAILED\n")

    print(WHITE + " RISK SCORE" + RESET)
    print(RED + "  ▸ FINAL SCORE : 1 / 10")
    print(GRAY + "  ▸ RISK LEVEL  : CRITICAL\n")

    print(WHITE + " SOC VERDICT" + RESET)
    print(RED + "  ▸ UNSAFE FOR REAL-WORLD USAGE\n")

    print(WHITE + " RECOMMENDATIONS" + RESET)
    print(SUCCESS + "  ▸ Use AES / RSA instead of classical ciphers")
    print(SUCCESS + "  ▸ Implement key exchange & IV")
    print(SUCCESS + "  ▸ Use authenticated encryption (AEAD)\n")

    banner_line()