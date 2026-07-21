"""functrait.py : function traits.

Simply speaking, % of Ti is a different from Ti.
While functions are often good to keep discrete, 
(although it might not look like that initially)
measuring them as traits requires continuity
 
That's why we present Functraits!
Also keeping Functrait 8-traital helps avoiding ipsativity.
The carrier is [0, 1]^8, indices follow convention from PSys.
"""

from dataclasses import dataclass, field
from jungian.trait import Trait
from jungian.dimension import Dimension

@dataclass(frozen=True)
class Functrait:
    """A continuous profile of function intensities."""
    ni: Trait = field(default_factory=lambda: Trait("Ni"))
    se: Trait = field(default_factory=lambda: Trait("Se"))
    ne: Trait = field(default_factory=lambda: Trait("Ne"))
    si: Trait = field(default_factory=lambda: Trait("Si"))
    fi: Trait = field(default_factory=lambda: Trait("Fi"))
    te: Trait = field(default_factory=lambda: Trait("Te"))
    fe: Trait = field(default_factory=lambda: Trait("Fe"))
    ti: Trait = field(default_factory=lambda: Trait("Ti"))

    def to_vector(self) -> list[Trait]:
        """Convert to an 8-traital list of functions"""
        return [self.ni, self.se, self.ne, self.si, self.fi, self.te, self.fe, self.ti]

    def scores(self) -> list[float]:
        """Return raw numeric scores (floats) for all 8 traits."""
        return [t.value.value for t in self.to_vector()] 


# NOTE: these functions are experimental
# for pure Ti this would return 0.625 for example
# even though intuitively you'd probably expect 1.0
# to "fix" this you would simply need to rely on "dominant" function
def phase(ft: Functrait) -> Trait:
    """Phase trait from Functrait"""
    values = ft.scores()
    ones = values[1] + values[3] + values[5] + values[7]
    zeros = values[0] + values[2] + values[4] + values[6]
    return Trait("Phase", Dimension((ones - zeros + 4.0) / 8.0))


def stance(ft: Functrait) -> Trait:
    """Stance trait from Functrait"""
    values = ft.scores()
    ones = values[2] + values[3] + values[6] + values[7]
    zeros = values[0] + values[1] + values[4] + values[5]
    return Trait("Stance", Dimension((ones - zeros + 4.0) / 8.0))


def mode(ft: Functrait) -> Trait:
    """Mode trait from Functrait"""
    values = ft.scores()
    ones = values[4] + values[5] + values[6] + values[7]
    zeros = values[0] + values[1] + values[2] + values[3]
    return Trait("Mode", Dimension((ones - zeros + 4.0) / 8.0))

# Introversion is Stance XNOR Phase
def attitude(ft: Functrait) -> Trait:
    """Attitude (introversion/extraversion) trait from Functrait"""
    s = stance(ft).value.value
    p = phase(ft).value.value
    return Trait("Attitude", Dimension(1.0 - abs(s - p)))
