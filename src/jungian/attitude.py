"""
attitude.py
"""

from enum import StrEnum


class Attitude(StrEnum):
    """Attitude class"""

    I = "i"
    E = "e"

    @property
    def symbol(self) -> str:
        """A crutch method to keep legacy code working for now"""
        return self.value
