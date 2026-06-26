"""
jungian : code for working with Jungian typology.
The top-level contains generic, theory‑agnostic Jungian typology base classes + implementations
"""

from .process import Process
from .attitude import Attitude
from .function import (
    Function,
    switch_attitude,
    switch_process,
    Ne,
    Ni,
    Se,
    Si,
    Te,
    Ti,
    Fe,
    Fi,
)
from .type import (
    Type,
    is_extraverted,
    is_introverted,
    is_sensing,
    is_intuitive,
    is_thinking,
    is_feeling,
    is_rational,
    is_irrational,
    from_dom_aux,
    to_dom_aux,
)

__all__ = [
    "Process",
    "Attitude",
    "Function",
    "switch_attitude",
    "switch_process",
    "Ne",
    "Ni",
    "Se",
    "Si",
    "Te",
    "Ti",
    "Fe",
    "Fi",
    "Type",
    "is_extraverted",
    "is_introverted",
    "is_sensing",
    "is_intuitive",
    "is_thinking",
    "is_feeling",
    "is_rational",
    "is_irrational",
    "from_dom_aux",
    "to_dom_aux",
]
