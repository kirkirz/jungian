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

def extremity(dimension: Dimension) -> float:
    """
    Return how extreme a continuous dimension score is (0.0 to 1.0).
    
    - 0.0 means perfectly balanced (score == 0.5)
    - 1.0 means maximally extreme (score == 0.0 or 1.0)
    Extremity is derived as: `extremity = abs(signed_deviation) * 2`
    """
    return abs(dimension.value - 0.5) * 2


def signed_deviation(d: Dimension) -> float:
    """
    Return the signed deviation from center (-0.5 to 0.5).
    
    - Negative means pole A (score < 0.5)
    - Positive means pole B (score > 0.5)
    - Magnitude indicates strength of deviation.
    """
    return d.value - 0.5


def bipolar_consistency(a: float, b: float) -> float:
    """
    Validate a pair of opposing raw scores (0.0 to 1.0).

    In a perfectly consistent response, a + b ≈ 1.0.
    - 1.0 = Perfectly consistent (sum == 1.0)
    - 0.0 = Maximally inconsistent (sum == 0.0 or 2.0)

    Examples:
        >>> bipolar_consistency(0.8, 0.2)  # Perfect
        1.0
        >>> bipolar_consistency(0.9, 0.8)  # Both high → bad
        0.1
        >>> bipolar_consistency(0.1, 0.2)  # Both low → bad
        0.1
    """
    return 1.0 - abs((a.value + b.value) - 1.0)
