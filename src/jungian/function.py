"""
function.py : work with Jungian cognitive functions.

Note: here function means process + attitude.
Originally, in Jung's works "function" means what we here call process.
In socionics "function" refers (roughly) to the position in the stack that IM elements occupy.
The usage of the term here diverges from both of them.

The equivalents are:
Jung : function + attitude (aka type)
Socionics : IM element
"""

from jungian.process import Process
from jungian.attitude import Attitude

class Function():
    """Generic cognitive function class"""

    def __init__(self, process: Process, attitude: Attitude):
        self.process = process
        self.attitude = attitude

    def __repr__(self) -> str:
        return f"{self.process}{self.attitude}"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Function):
            return False
        return self.process == other.process and self.attitude == other.attitude

    def __hash__(self):
        return hash((self.process, self.attitude))
