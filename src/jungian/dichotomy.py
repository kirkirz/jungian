"""Dichotomy engine"""

from dataclasses import dataclass
from typing import Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from jungian.type import Type


@dataclass(frozen=True)
class Dichotomy:
    """A Dichotomy is a predicate on Type"""

    name: str
    predicate: Callable[["Type"], bool]

    def __call__(self, t: "Type") -> bool:
        return self.predicate(t)

    def __mul__(self, other: "Dichotomy") -> "Dichotomy":
        """XNOR operator: (X == Y). Often denoted as *"""
        return Dichotomy(
            name=f"{self.name}*{other.name}", predicate=lambda t: self(t) == other(t)
        )

    def __and__(self, other: "Dichotomy") -> "Dichotomy":
        """Logical AND."""
        return Dichotomy(
            name=f"{self.name}&{other.name}", predicate=lambda t: self(t) and other(t)
        )

    def __or__(self, other: "Dichotomy") -> "Dichotomy":
        """Logical OR."""
        return Dichotomy(
            name=f"{self.name}|{other.name}", predicate=lambda t: self(t) or other(t)
        )

    def __xor__(self, other: "Dichotomy") -> "Dichotomy":
        """Logical XOR."""
        return Dichotomy(
            name=f"{self.name}^{other.name}", predicate=lambda t: self(t) != other(t)
        )

    def __invert__(self) -> "Dichotomy":
        """Logical NOT."""
        return Dichotomy(name=f"~{self.name}", predicate=lambda t: not self(t))

    def __repr__(self) -> str:
        return f"Dichotomy({self.name})"

    def __str__(self) -> str:
        return self.name


E = Dichotomy("E", lambda t: t.e_i == "E")
I = Dichotomy("I", lambda t: t.e_i == "I")
N = Dichotomy("N", lambda t: t.s_n == "N")
S = Dichotomy("S", lambda t: t.s_n == "S")
T = Dichotomy("T", lambda t: t.t_f == "T")
F = Dichotomy("F", lambda t: t.t_f == "F")
j = Dichotomy("J", lambda t: t.j_p == "j")
p = Dichotomy("P", lambda t: t.j_p == "p")

J = E * j
P = E * p
