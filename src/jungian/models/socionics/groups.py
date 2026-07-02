"""Small groups for socionics"""
from typing import TYPE_CHECKING
from jungian.models.socionics.reinin import *

if TYPE_CHECKING:
    from jungian.type import Type

# Clubs
NT = Researchers = N & T
NF = Humanitarians = N & F
ST = Pragmatists = S & T
SF = Socials = S & F


def club(t: Type) -> str:
    """Return the club of a Type."""
    if NT(t):
        return "NT"
    if NF(t):
        return "NF"
    if ST(t):
        return "ST"
    if SF(t):
        return "SF"
    raise ValueError(f"Type {t} does not belong to any club")


# Gulenko temperaments
Ep = E & p
Ej = E & j
Ip = I & p
Ij = I & j

# Communication styles
EF = E & F
IF = I & F
ET = E & T
IT = I & T

# Argumentation styles
Tp = T & p
Fj = F & j
Tj = T & j
Fp = F & p

# Romance styles
# Se in Ego block
Aggressor = S & Static
# Ne in Ego block
Childlike = N & Static
# Si in Ego block
Caregiver = S & Dynamic
# Ni in Ego block
Victim = N & Dynamic

# Quadras
Alpha = Reasonable & Subjectivist
Beta = Resolute & Subjectivist
Gamma = Resolute & Objectivist
Delta = Reasonable & Objectivist


def quadra(t: Type) -> str:
    """Return the quadra of a Type."""
    if Alpha(t):
        return "Alpha"
    if Beta(t):
        return "Beta"
    if Gamma(t):
        return "Gamma"
    if Delta(t):
        return "Delta"
    raise ValueError(f"Type {t} does not belong to any quadra")
