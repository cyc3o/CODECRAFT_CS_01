"""
CAESAR CIPHER ENGINE — CORE
Author : Vishal
Domain : Cryptography | Cryptanalysis | SOC Lab
"""

import string


# =========================================================
# CAESAR CIPHER CLASS
# =========================================================
class Caesar:
    """
    Caesar cipher engine with encryption, decryption,
    and brute-force analysis support.
    """

    def __init__(self, shift: int):
        # Normalize shift to 0–25
        self.shift = shift % 26

    # -----------------------------------------------------
    # ENCRYPTION
    # -----------------------------------------------------
    def enc(self, text: str) -> str:
        """
        Encrypt plaintext using Caesar cipher
        """
        return self._shift(text, self.shift)

    # -----------------------------------------------------
    # DECRYPTION
    # -----------------------------------------------------
    def dec(self, text: str) -> str:
        """
        Decrypt ciphertext using Caesar cipher
        """
        return self._shift(text, -self.shift)

    # -----------------------------------------------------
    # INTERNAL SHIFT LOGIC
    # -----------------------------------------------------
    def _shift(self, text: str, shift: int) -> str:
        """
        Core shifting logic (case-preserving)
        """
        result = []

        for char in text:
            if char.isalpha():
                if char.isupper():
                    alphabet = string.ascii_uppercase
                else:
                    alphabet = string.ascii_lowercase

                index = alphabet.index(char)
                result.append(alphabet[(index + shift) % 26])
            else:
                # Preserve numbers, symbols, spaces
                result.append(char)

        return "".join(result)

    # -----------------------------------------------------
    # BRUTE FORCE ENGINE (STATIC)
    # -----------------------------------------------------
    @staticmethod
    def brute(ciphertext: str):
        """
        Brute-force Caesar cipher with basic scoring
        Returns sorted list of (shift, plaintext, score)
        """
        results = []

        common_words = ["THE", "AND", "IS", "TO", "OF"]

        for shift in range(1, 26):
            plaintext = Caesar(shift).dec(ciphertext)
            score = sum(
                1 for word in common_words
                if word in plaintext.upper()
            )

            results.append((shift, plaintext, score))

        # Highest score first
        results.sort(key=lambda x: x[2], reverse=True)
        return results