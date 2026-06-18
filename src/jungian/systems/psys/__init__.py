"""
PSys implementations
"""

from .vector import Vector, xor, vectorise, devectorise

# Aliases for direct access to the enum members (matching generic naming)
Ti = Vector.TI
Te = Vector.TE
Fi = Vector.FI
Fe = Vector.FE
Ni = Vector.NI
Ne = Vector.NE
Si = Vector.SI
Se = Vector.SE

__all__ = [
    "Vector",
    "xor",
    "vectorise",
    "devectorise",
    "Ti", "Te", "Fi", "Fe",
    "Ni", "Ne", "Si", "Se",
]
