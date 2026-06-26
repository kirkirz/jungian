"""Dichotomy engine"""

from dataclasses import dataclass
from typing import Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from jungian.type import Type


@dataclass(frozen=True)
class Dichotomy:
    """A Dichotomy is a predicate on Type"""
    name: str
    predicate: Callable[['Type'], bool]

    def __call__(self, t: 'Type') -> bool:
        return self.predicate(t)

    def __mul__(self, other: 'Dichotomy') -> 'Dichotomy':
        """XNOR operator: (X == Y). Often denoted as *"""
        return Dichotomy(
            name=f"{self.name}*{other.name}",
            predicate=lambda t: self(t) == other(t)
        )

    def __and__(self, other: 'Dichotomy') -> 'Dichotomy':
        """Logical AND."""
        return Dichotomy(
            name=f"{self.name}&{other.name}",
            predicate=lambda t: self(t) and other(t)
        )

    def __or__(self, other: 'Dichotomy') -> 'Dichotomy':
        """Logical OR."""
        return Dichotomy(
            name=f"{self.name}|{other.name}",
            predicate=lambda t: self(t) or other(t)
        )

    def __xor__(self, other: 'Dichotomy') -> 'Dichotomy':
        """Logical XOR."""
        return Dichotomy(
            name=f"{self.name}^{other.name}",
            predicate=lambda t: self(t) != other(t)
        )

    def __invert__(self) -> 'Dichotomy':
        """Logical NOT."""
        return Dichotomy(
            name=f"~{self.name}",
            predicate=lambda t: not self(t)
        )

    def __repr__(self) -> str:
        return f"Dichotomy({self.name})"

    def __str__(self) -> str:
        return self.name
