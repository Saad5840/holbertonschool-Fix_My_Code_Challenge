#!/usr/bin/python3
"""
User class with password hashing using only the Python standard library.
No external deps (works on Ubuntu 20.04 graders).
"""

import hashlib
import hmac
import os


class User:
    def __init__(self, name):
        self.__name = name
        # Store as "hexsalt$hexhash"
        self.__password = None

    @property
    def name(self):
        return self.__name

    def set_password(self, password: str) -> None:
        """Hash and store the password with a random salt."""
        if password is None:
            raise ValueError("Password cannot be None")
        # 16-byte random salt
        salt = os.urandom(16)
        digest = hashlib.sha256(salt + password.encode("utf-8")).hexdigest()
        self.__password = f"{salt.hex()}${digest}"

    def is_valid_password(self, password: str) -> bool:
        """Validate a plaintext password against the stored salted hash."""
        if self.__password is None or password is None:
            return False
        try:
            salt_hex, stored_hex = self.__password.split("$", 1)
        except ValueError:
            # Corrupted storage format
            return False
        salt = bytes.fromhex(salt_hex)
        candidate_hex = hashlib.sha256(salt + password.encode("utf-8")).hexdigest()
        # Constant-time comparison
        return hmac.compare_digest(candidate_hex, stored_hex)


if __name__ == "__main__":
    # No prints here — main_0.py will run the tests and print the expected line.
    pass

