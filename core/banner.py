"""
BANNER MODULE — ORIGINAL ASCII
Author : Vishal
Domain : SOC | Cryptanalysis | Forensics
"""

from utils.colors import BROWN, ORANGE, GRAY, RESET
from utils.helpers import banner_line


def banner():
    print(BROWN + r"""
　　　　╭╮╭╮
            ┃┃┃┃
            ┃┃┃┃
         ╭╯┗╯┃
         ┃▋　▋┃
         ▇
         ╰╮
      ╭╭━╯      ┃
   ╱╰╰╯╲　   ┃
▕╭╭╮╮╮▏   ┃         @cyc3o
▕▔▔▔▔▔▏   ┃
　╲▁▁▁╱╭　┣╮
      ╭　╭━┛　┣╯
      ╰━╰━━━╯
""" + RESET)

    print(ORANGE + " ADVANCED CAESAR CIPHER LAB — BRUTAL EDITION" + RESET)
    print(GRAY   + " SOC | CRYPTANALYSIS | FORENSICS | AUDIT MODE" + RESET)
    banner_line()