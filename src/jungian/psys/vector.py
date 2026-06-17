"""vector.py : PSys implementation of Function"""

from enum import IntEnum
from jungian import Function, Process, Attitude


class Vector(IntEnum):
    """PSys Vector class"""

    NI = 0b000
    NE = 0b010
    SI = 0b011
    SE = 0b001
    FI = 0b100
    FE = 0b110
    TI = 0b111
    TE = 0b101

    @property
    def bits(self) -> tuple[int, int, int]:
        """Get full Vector bits tuple"""
        return ((self.value >> 2) & 1, (self.value >> 1) & 1, self.value & 1)

    @property
    def mode(self) -> int:
        """Mode"""
        return (self.value >> 2) & 1

    @property
    def stance(self) -> int:
        """Stance"""
        return (self.value >> 1) & 1

    @property
    def phase(self) -> int:
        """Phase"""
        return self.value & 1


def xor(a: Vector, b: Vector) -> Vector:
    """Explicit XOR operation for Vectors"""
    return Vector(a ^ b)


def vectorise(fn):
    """Convert Function to Vector"""
    if isinstance(fn, str):
        return Vector[fn.upper()]
    try:
        proc = str(fn.process)
        att = str(fn.attitude)
    except AttributeError:
        raise TypeError(...)
    return Vector[f"{proc}{att}".upper()]


def devectorise(v: Vector) -> Function:
    """Convert Vector to Function"""
    name = v.name
    return Function(Process(name[0]), Attitude(name[1].lower()))
