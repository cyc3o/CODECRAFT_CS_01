"""
ACCESS CONTROL MODULE — SOC
Author : Vishal
Domain : SOC | Training Lab | Initialization Gate
"""

from utils.colors import ORANGE, GRAY, RESET
from utils.helpers import banner_line


# =========================================================
# LOGIN / ACCESS GATE (TRAINING MODE)
# =========================================================
def login():
    """
    SOC startup access gate (NO AUTHENTICATION)
    Used for local training / GitHub projects
    """
    banner_line()
    print(ORANGE + " ACCESS CONTROL : DISABLED" + RESET)
    print(GRAY   + " MODE           : LOCAL SOC TRAINING LAB" + RESET)
    banner_line()
    return True