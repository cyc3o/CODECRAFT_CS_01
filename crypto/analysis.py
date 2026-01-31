"""
CRYPTO ANALYSIS MODULE - ANALYST ASSIST MODE
Author : Vishal
Domain : Cryptanalysis | SOC Analysis
"""

from collections import Counter
from crypto.caesar import Caesar
from utils.colors import ORANGE, WHITE, GRAY, RED, SUCCESS, RESET
from utils.helpers import banner_line


# =========================================================
# CONFIDENCE SCORING
# =========================================================
COMMON_WORDS = ["THE", "AND", "IS", "TO", "OF", "YOU", "THAT", "FOR"]


def confidence_label(score):
    if score >= 3:
        return "HIGH"
    elif score == 2:
        return "MEDIUM"
    elif score == 1:
        return "LOW"
    return "VERY LOW"


# =========================================================
# FREQUENCY ANALYSIS
# =========================================================
def frequency_analysis(text):
    banner_line()
    print(ORANGE + " FREQUENCY ANALYSIS - ANALYST VIEW" + RESET)
    banner_line()

    if len(text) < 20:
        print(RED + " WARNING: SHORT INPUT, LOW CONFIDENCE" + RESET)

    freq = Counter(c for c in text.upper() if c.isalpha())
    total = sum(freq.values())

    if total == 0:
        print(RED + " NO ANALYZABLE DATA" + RESET)
        return

    for char, count in freq.most_common():
        percent = (count / total) * 100
        print(WHITE + f" {char} : {percent:.2f}%" + RESET)

    print(GRAY + "\n ANALYST NOTES:" + RESET)
    print(GRAY + " - LIKELY ENGLISH LANGUAGE" + RESET)
    print(GRAY + " - CORRELATE WITH AUTO CRACK RESULTS" + RESET)
    banner_line()


# =========================================================
# AUTO CRACK (RANKED RESULTS)
# =========================================================
def auto_crack(ciphertext):
    banner_line()
    print(ORANGE + " AUTO CRACK - RANKED POSSIBILITIES" + RESET)
    banner_line()

    if len(ciphertext) < 15:
        print(RED + " WARNING: CIPHERTEXT TOO SHORT" + RESET)

    results = []

    for shift in range(1, 26):
        plain = Caesar(shift).dec(ciphertext)
        score = sum(1 for w in COMMON_WORDS if w in plain.upper())
        results.append((shift, plain, score))

    results.sort(key=lambda x: x[2], reverse=True)

    for shift, text, score in results[:5]:
        label = confidence_label(score)
        color = SUCCESS if label == "HIGH" else WHITE

        print(
            color +
            f" [{label}] SHIFT {shift} -> {text.upper()}" +
            RESET
        )

    print(GRAY + "\n ANALYST DECISION REQUIRED" + RESET)
    print(GRAY + " TOOL DOES NOT SELECT FINAL ANSWER" + RESET)
    banner_line()