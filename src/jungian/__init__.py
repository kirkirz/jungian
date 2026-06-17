"""
jungian : code for working with Jungian typology.
The top-level contains generic, theory‑agnostic Jungian typology base classes + implementations
"""

from .process import Process
from .attitude import Attitude
from .function import Function
from .type import Type

__all__ = ["Process", "Attitude", "Function", "Type"]
