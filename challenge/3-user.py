#!/usr/bin/python3
"""
User class with secure password hashing and validation.
"""

import bcrypt


class User:
    def __init__(self, name):
        self.__name = name
        self.__password = None

    @property
    def name(self):
        return self.__name

    def set_password(self, password: str) -> None:
        """Hash and store the password securely."""
        if password is None:
            raise ValueError("Password cannot be None")
        # bcrypt requires bytes
        self.__password = bcrypt.hashpw(password.encode('utf-8'),
                                        bcrypt.gensalt())

    def is_valid_password(self, password: str) -> bool:
        """Check if a plain-text password matches the stored hash."""
        if self.__password is None or password is None:
            return False
        return bcrypt.checkpw(password.encode('utf-8'), self.__password)


if __name__ == "__main__":
    user = User("Test User")
    user.set_password("MyPass123")
    assert user.is_valid_password("MyPass123") is True
    assert user.is_valid_password("wrongpass") is False
    print("All tests passed!")
