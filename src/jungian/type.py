"""
type.py - generic Jungian type object (theory-independent).

Note: originally Jung called types what we nowadays call "functions"/"IMEs" etc (depends on specific theory).

Note: this module uses rationality/irrationality (j/p) instead of MBTI's J/P for canonical representation.
"""

from dataclasses import dataclass
from typing import Literal


@dataclass(frozen=True)
class Type:
    """Four-dichotomy type (E/I, S/N, T/F, j/p) where j = rational, p = irrational."""

    e_i: Literal["E", "I"]
    s_n: Literal["S", "N"]
    t_f: Literal["T", "F"]
    j_p: Literal["j", "p"]

    def __post_init__(self):
        valid_ei = {"E", "I"}
        valid_sn = {"S", "N"}
        valid_tf = {"T", "F"}
        valid_jp = {"j", "p"}
        if self.e_i not in valid_ei:
            raise ValueError(f"e_i must be E or I, got {self.e_i}")
        if self.s_n not in valid_sn:
            raise ValueError(f"s_n must be S or N, got {self.s_n}")
        if self.t_f not in valid_tf:
            raise ValueError(f"t_f must be T or F, got {self.t_f}")
        if self.j_p not in valid_jp:
            raise ValueError(f"j_p must be j or p, got {self.j_p}")

    def __repr__(self):
        return f"{self.e_i}{self.s_n}{self.t_f}{self.j_p}"
