"""Continuous traits"""

from dataclasses import dataclass
from jungian.dimension import Dimension


@dataclass(frozen=True)
class Trait:
    """A named continuous axis."""

    name: str
    value: Dimension = Dimension()

    def __and__(self, other: "Trait") -> "Trait":
        return Trait(f"({self.name}&{other.name})", self.value & other.value)

    def __or__(self, other: "Trait") -> "Trait":
        return Trait(f"({self.name}|{other.name})", self.value | other.value)

    def __invert__(self) -> "Trait":
        return Trait(f"~{self.name}", ~self.value)

    def __xor__(self, other: "Trait") -> "Trait":
        return Trait(f"({self.name}^{other.name})", self.value ^ other.value)

    def __mul__(self, other: "Trait") -> "Trait":
        # XNOR / equivalence
        return Trait(f"({self.name}*{other.name})", self.value * other.value)

    def __repr__(self) -> str:
        return f"Trait({self.name}, {self.value.value:.3f})"
