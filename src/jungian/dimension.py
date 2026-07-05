"""
dimension.py – Continuous trait representation.
"""

from dataclasses import dataclass
from typing import Optional

@dataclass
class Dimension:
    """Dimension class"""

    name: str
    value: Optional[float] = None

    def __post_init__(self) -> None:
        if not 0.0 <= self.value <= 1.0:
            raise ValueError(f"Value must be in [0, 1], got {self.value}")

    def __and__(self, other: "Dimension") -> "Dimension":
        return Dimension(f"({self.name}&{other.name})", min(self.value, other.value))

    def __or__(self, other: "Dimension") -> "Dimension":
        return Dimension(f"({self.name}|{other.name})", max(self.value, other.value))

    def __invert__(self) -> "Dimension":
        return Dimension(f"~{self.name}", 1.0 - self.value)

    def __xor__(self, other: "Dimension") -> "Dimension":
        return Dimension(f"({self.name}^{other.name})", abs(self.value - other.value))

    def __mul__(self, other: "Dimension") -> "Dimension":
        # XNOR = equivalence (1 - |a-b|)
        return Dimension(
            f"({self.name}*{other.name})", 1.0 - abs(self.value - other.value)
        )

    def __repr__(self) -> str:
        return f"Dimension({self.name}, {self.value:.3f})"
