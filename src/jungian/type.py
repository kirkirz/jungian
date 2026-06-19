"""
type.py - generic Jungian type object (theory-independent).

Note: originally Jung called types what we nowadays call "functions"/"IMEs" etc
(depends on specific theory).

Note: this module uses rationality/irrationality (j/p)
instead of MBTI's J/P for canonical representation.
"""

from dataclasses import dataclass
from typing import Literal
from jungian.function import Function
from jungian.process import Process
from jungian.attitude import Attitude


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


# Explicit type predicates:


def is_extraverted(t: Type) -> bool:
    return t.e_i == "E"


def is_introverted(t: Type) -> bool:
    return t.e_i == "I"


def is_sensing(t: Type) -> bool:
    return t.s_n == "S"


def is_intuitive(t: Type) -> bool:
    return t.s_n == "N"


def is_thinking(t: Type) -> bool:
    return t.t_f == "T"


def is_feeling(t: Type) -> bool:
    return t.t_f == "F"


def is_rational(t: Type) -> bool:
    return t.j_p == "j"


def is_irrational(t: Type) -> bool:
    return t.j_p == "p"


# These conversions are included, since they're often used:


def from_dom_aux(dominant: Function, auxiliary: Function) -> Type:
    """Derive a Type from dominant and auxiliary functions."""
    dom_is_j = dominant.process.symbol in ("T", "F")
    aux_is_j = auxiliary.process.symbol in ("T", "F")
    if dom_is_j == aux_is_j:
        raise ValueError(
            "One function must be judging (T/F) and the other perceiving (S/N)"
        )

    e_i = "I" if dominant.attitude.symbol == "i" else "E"
    j_p = "j" if dom_is_j else "p"

    if dom_is_j:
        t_f = dominant.process.symbol
        s_n = auxiliary.process.symbol
    else:
        s_n = dominant.process.symbol
        t_f = auxiliary.process.symbol

    return Type(e_i=e_i, s_n=s_n, t_f=t_f, j_p=j_p)


def to_dom_aux(t: Type) -> tuple[Function, Function]:
    """Return (dominant, auxiliary) functions from a Type."""
    is_dom_j = t.j_p == "j"
    dom_sym = t.t_f if is_dom_j else t.s_n
    aux_sym = t.s_n if is_dom_j else t.t_f

    dom_att = "i" if t.e_i == "I" else "e"
    aux_att = "e" if t.e_i == "I" else "i"

    return (
        Function(Process(dom_sym), Attitude(dom_att)),
        Function(Process(aux_sym), Attitude(aux_att)),
    )


# Type aliases:
ENTp = Type("E", "N", "T", "p")
INTp = Type("I", "N", "T", "p")
ENTj = Type("E", "N", "T", "j")
INTj = Type("I", "N", "T", "j")
ENFp = Type("E", "N", "F", "p")
INFp = Type("I", "N", "F", "p")
ENFj = Type("E", "N", "F", "j")
INFj = Type("I", "N", "F", "j")
ESTp = Type("E", "S", "T", "p")
ISTp = Type("I", "S", "T", "p")
ESTj = Type("E", "S", "T", "j")
ISTj = Type("I", "S", "T", "j")
ESFp = Type("E", "S", "F", "p")
ISFp = Type("I", "S", "F", "p")
ESFj = Type("E", "S", "F", "j")
ISFj = Type("I", "S", "F", "j")
