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


class Function:
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


def switch_attitude(f: Function) -> Function:
    """Return a new Function with the opposite attitude"""
    new_att = Attitude("e" if f.attitude.symbol == "i" else "i")
    return Function(f.process, new_att)


def switch_process(f: Function) -> Function:
    """Toggle the process, within the same mode"""
    process_map = {"N": "S", "S": "N", "T": "F", "F": "T"}
    new_proc = Process(process_map[f.process.symbol])
    return Function(new_proc, f.attitude)


# Predefined constants for convenience
Ne = Function(Process("N"), Attitude("e"))
Ni = Function(Process("N"), Attitude("i"))
Se = Function(Process("S"), Attitude("e"))
Si = Function(Process("S"), Attitude("i"))
Te = Function(Process("T"), Attitude("e"))
Ti = Function(Process("T"), Attitude("i"))
Fe = Function(Process("F"), Attitude("e"))
Fi = Function(Process("F"), Attitude("i"))
