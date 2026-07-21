"""Small groups for socionics"""

from enum import StrEnum
from functools import lru_cache
from typing import Callable
from jungian.type import Type
from jungian.dichotomy import Dichotomy
# fmt: off
from jungian.models.socionics.reinin import (
    N, S,
    T, F,
    E, I,
    j, p,
    Static, Dynamic,
    Reasonable, Subjectivist,
    Resolute, Objectivist,
)
# fmt: on


# Factory
def group[G: StrEnum](registry: dict[G, Dichotomy]) -> Callable[[Type], G]:
    """Factory that returns a memoized dispatcher for group membership."""

    @lru_cache(maxsize=None)
    def lookup(t: Type) -> G:
        for key, pred in registry.items():
            if pred(t):
                return key
        raise LookupError(
            f"Type {t} does not belong to any group in {list(registry.keys())}"
        )

    return lookup


# Enums
class Quadra(StrEnum):
    ALPHA = "Alpha"
    BETA = "Beta"
    GAMMA = "Gamma"
    DELTA = "Delta"


class Club(StrEnum):
    NT = "NT"
    NF = "NF"
    ST = "ST"
    SF = "SF"


class Temperament(StrEnum):
    Ep = "Ep"
    Ej = "Ej"
    Ip = "Ip"
    Ij = "Ij"


class RomanceStyle(StrEnum):
    AGGRESSOR = "Aggressor"
    CHILDLIKE = "Childlike"
    CAREGIVER = "Caregiver"
    VICTIM = "Victim"


class CommunicationStyle(StrEnum):
    EF = "EF"
    IF = "IF"
    ET = "ET"
    IT = "IT"


class ArgumentationStyle(StrEnum):
    Tp = "Tp"
    Fj = "Fj"
    Tj = "Tj"
    Fp = "Fp"


# Predicates:
## Clubs
NT = Researchers = N & T
NF = Humanitarians = N & F
ST = Pragmatists = S & T
SF = Socials = S & F

## Gulenko temperaments
Ep = E & p
Ej = E & j
Ip = I & p
Ij = I & j

## Communication styles
EF = E & F
IF = I & F
ET = E & T
IT = I & T

## Argumentation styles
Tp = T & p
Fj = F & j
Tj = T & j
Fp = F & p

## Romance styles
Aggressor = S & Static  # Se in Ego block
Childlike = N & Static  # Ne in Ego block
Caregiver = S & Dynamic  # Si in Ego block
Victim = N & Dynamic  # Ni in Ego block

# Quadras
Alpha = Reasonable & Subjectivist
Beta = Resolute & Subjectivist
Gamma = Resolute & Objectivist
Delta = Reasonable & Objectivist


# Dispatchers:
CLUBS = {
    Club.NT: NT,
    Club.NF: NF,
    Club.ST: ST,
    Club.SF: SF,
}
club = group(CLUBS)

TEMPERAMENTS = {
    Temperament.Ep: Ep,
    Temperament.Ej: Ej,
    Temperament.Ip: Ip,
    Temperament.Ij: Ij,
}
temperament = group(TEMPERAMENTS)

COMMUNICATION_STYLES = {
    CommunicationStyle.EF: EF,
    CommunicationStyle.IF: IF,
    CommunicationStyle.ET: ET,
    CommunicationStyle.IT: IT,
}
communication_style = group(COMMUNICATION_STYLES)

ARGUMENTATION_STYLES = {
    ArgumentationStyle.Tp: Tp,
    ArgumentationStyle.Fj: Fj,
    ArgumentationStyle.Tj: Tj,
    ArgumentationStyle.Fp: Fp,
}
argumentation_style = group(ARGUMENTATION_STYLES)

ROMANCE_STYLES = {
    RomanceStyle.AGGRESSOR: Aggressor,
    RomanceStyle.CHILDLIKE: Childlike,
    RomanceStyle.CAREGIVER: Caregiver,
    RomanceStyle.VICTIM: Victim,
}
romance_style = group(ROMANCE_STYLES)

QUADRAS = {
    Quadra.ALPHA: Alpha,
    Quadra.BETA: Beta,
    Quadra.GAMMA: Gamma,
    Quadra.DELTA: Delta,
}
quadra = group(QUADRAS)
