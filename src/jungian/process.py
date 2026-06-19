"""
process.py : Generic process object.
"""

from typing import Literal


class Process:
    """Process class"""

    def __init__(self, symbol: Literal["N", "S", "T", "F"]):
        if symbol not in ("N", "T", "F", "S"):
            raise ValueError(
                f"Invalid Process symbol: {symbol}. Must be 'N', 'T', 'F' or 'S'"
            )
        self.symbol = symbol

    def __repr__(self) -> str:
        return self.symbol

    def __eq__(self, other) -> bool:
        if not isinstance(other, Process):
            return False
        return self.symbol == other.symbol

    def __hash__(self) -> int:
        return hash(self.symbol)
