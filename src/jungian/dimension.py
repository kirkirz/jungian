"""
dimension.py – Continuous trait representation.
"""

from dataclasses import dataclass

@dataclass(frozen=True)
class Dimension:
    """A scalar value in [0, 1]."""
    value: float = 0.5

    def __post_init__(self) -> None:
        if not 0.0 <= self.value <= 1.0:
            raise ValueError(f"Value must be in [0, 1], got {self.value}")

    def __and__(self, other: "Dimension") -> "Dimension":
        return Dimension(min(self.value, other.value))

    def __or__(self, other: "Dimension") -> "Dimension":
        return Dimension(max(self.value, other.value))

    def __invert__(self) -> "Dimension":
        return Dimension(1.0 - self.value)

    def __xor__(self, other: "Dimension") -> "Dimension":
        return Dimension(abs(self.value - other.value))

    def __mul__(self, other: "Dimension") -> "Dimension":
        # XNOR = equivalence (1 - |a-b|)
        return Dimension(1.0 - abs(self.value - other.value))

    def __repr__(self) -> str:
        return f"Dimension({self.value:.3f})"
