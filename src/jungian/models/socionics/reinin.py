"""Reinin dichotomies"""

from jungian.dichotomy import Dichotomy, E, N, T, p, I, S, F, j

Static = E * p
Dynamic = ~Static

Democratic = N * T
Aristocratic = ~Democratic

Positivist = E * N * T
Negativist = ~Positivist

Tactical = N * p
Strategic = ~Tactical

Constructivist = T * p
Emotivist = ~Constructivist

Reasonable = E * N * p  # aka Judicious, Peripheral
Resolute = ~Reasonable  # aka Decisive, Central

Subjectivist = E * T * p  # aka Merry, Ascending
Objectivist = ~Subjectivist  # aka Serious, Descending

Process = N * T * p  # aka Right, Evolutory
Result = ~Process  # aka Left, Involutory

Questioner = E * N * T * p
Declarer = ~Questioner

Carefree = E * N  # aka Incidental
Farsighted = ~Carefree  # aka Cautious

Yielding = E * T
Obstinate = ~Yielding


def order(d: Dichotomy) -> int:
    """
    Return the order of a Reinin dichotomy.

    The order is the number of Jungian dichotomies (E, I, N, S, T, F, j, p)
    that compose it.

    Examples:
        >>> order(Static)    # E * p → 2
        2
        >>> order(Positivist) # E * N * T → 3
        3
        >>> order(Questioner) # E * N * T * p → 4
        4
    """
    return d.name.count("*") + 1


# fmt: off
REININ_TRAITS = (
    Static, Dynamic,
    Democratic, Aristocratic,
    Positivist, Negativist,
    Tactical, Strategic,
    Constructivist, Emotivist,
    Reasonable, Resolute,
    Subjectivist, Objectivist,
    Process, Result,
    Questioner, Declarer,
    Carefree, Farsighted,
    Yielding, Obstinate,
    # Jungian basis:
    E, I, N, S, T, F, j, p
)
# fmt: on
