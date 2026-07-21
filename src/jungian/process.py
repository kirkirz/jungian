"""
process.py : Generic process object.
"""

from enum import StrEnum


class Process(StrEnum):
    """Process class"""

    N = "N"
    T = "T"
    F = "F"
    S = "S"

    @property
    def symbol(self) -> str:
        """A crutch method to keep legacy code working for now"""
        return self.value
