"""Reinin dichotomies"""

from jungian.type import Type
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
