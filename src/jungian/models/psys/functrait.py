"""functrait.py : function traits.

Simply speaking, % of Ti is a different from Ti.
While functions are often good to keep discrete, 
(although it might not look like that initially)
measuring them as traits requires continuity
 
That's why we present Functraits!
Also keeping Functrait 8-dimensional helps avoiding ipsativity.
The carrier is [0, 1]^8, indices follow convention from PSys.
"""

from dataclasses import dataclass, field
from jungian.dimension import Dimension


@dataclass(frozen=True)
class Functrait:
    """A continuous profile of function intensities."""
    ni: Dimension = field(default_factory=lambda: Dimension("Ni"))
    se: Dimension = field(default_factory=lambda: Dimension("Se"))
    ne: Dimension = field(default_factory=lambda: Dimension("Ne"))
    si: Dimension = field(default_factory=lambda: Dimension("Si"))
    fi: Dimension = field(default_factory=lambda: Dimension("Fi"))
    te: Dimension = field(default_factory=lambda: Dimension("Te"))
    fe: Dimension = field(default_factory=lambda: Dimension("Fe"))
    ti: Dimension = field(default_factory=lambda: Dimension("Ti"))

    def to_vector(self) -> list[Dimension]:
        """Convert to an 8-dimensional list of functions"""
        return [self.ni, self.se, self.ne, self.si, self.fi, self.te, self.fe, self.ti]


# NOTE: these functions are experimental
# for pure Ti this would return 0.625 for example
# even though intuitively you'd probably expect 1.0
# to "fix" this you would simply need to rely on "dominant" function
def phase(ft: Functrait) -> Dimension:
    """Phase dimension from Functrait"""
    values = [d.value for d in ft.to_vector()]
    ones = values[1] + values[3] + values[5] + values[7]
    zeros = values[0] + values[2] + values[4] + values[6]
    return Dimension("Phase", (ones - zeros + 4.0) / 8.0)


def stance(ft: Functrait) -> Dimension:
    """Stance dimension from Functrait"""
    values = [d.value for d in ft.to_vector()]
    ones = values[2] + values[3] + values[6] + values[7]
    zeros = values[0] + values[1] + values[4] + values[5]
    return Dimension("Stance", (ones - zeros + 4.0) / 8.0)


def mode(ft: Functrait) -> Dimension:
    """Mode dimension from Functrait"""
    values = [d.value for d in ft.to_vector()]
    ones = values[4] + values[5] + values[6] + values[7]
    zeros = values[0] + values[1] + values[2] + values[3]
    return Dimension("Mode", (ones - zeros + 4.0) / 8.0)

# Introversion is Stance XNOR Phase
def attitude(ft: Functrait) -> Dimension:
    """Attitude (introversion/extraversion) dimension from Functrait"""
    s = stance(ft).value
    p = phase(ft).value
    return Dimension("Attitude", 1.0 - abs(s - p))
