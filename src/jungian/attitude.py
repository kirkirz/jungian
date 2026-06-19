"""
attitude.py
"""

from typing import Literal


class Attitude:
    """Attitude class"""

    def __init__(self, symbol: Literal["i", "e"]):
        if symbol not in ("i", "e"):
            raise ValueError(f"Invalid Attitude symbol: {symbol}. Must be 'i' or 'e'.")
        self.symbol = symbol

    def __repr__(self) -> str:
        return self.symbol

    def __eq__(self, other) -> bool:
        if not isinstance(other, Attitude):
            return False
        return self.symbol == other.symbol

    def __hash__(self) -> int:
        return hash(self.symbol)
