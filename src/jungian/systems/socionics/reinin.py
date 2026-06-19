from jungian.type import Type
# 2/11 dichotomies implemented as of now (excluding Jungian foundation)
def is_democratic(t: Type) -> bool:
    """Return True if the Type is Democratic (Reinin trait)."""
    return (t.s_n == "N") == (t.t_f == "T")

def is_aristocratic(t: Type) -> bool:
    """Return True if the Type is Aristocratic"""
    return not is_democratic(t)

def is_positivist(t: Type) -> bool:
    """Return True if the Type is Positivist (Reinin trait)."""
    return (t.s_n == "N") == (t.t_f == "T") == (t.e_i == "E")

def is_negativist(t: Type) -> bool:
    """Return True if the Type is Negativist"""
    return not is_positivist(t)

# These should be fixed/verified by someone:
# def is_process(t: Type) -> bool:
#    return (t.s_n == "N") == (t.s_n == "P")
#
# def is_carefree(t: Type) -> bool:
#    return (t.e_i == "E") == (t.s_n == "N")
#
# def is_yielding(t: Type) -> bool:
#    return (t.e_i == "E") == (t.t_f == "T")
#
# def is_obstinate(t: Type) -> bool:
#    return not is_yielding(t)
#
# def is_static(t: Type) -> bool:
#    return (t.e_i == "E") == (t.s_n == "P")
#
# def is_subjectivist(t: Type) -> bool:
#    return (t.e_i == "E") == (t.t_f == "T")  == (t.s_n == "P")
#
# def is_process(t: Type) -> bool:
#    return (t.s_n == "N") == (t.t_f == "T")  == (t.s_n == "P")
#
# def is_constructivist(t: Type) -> bool:
#    return (t.t_f == "T") == (t.s_n == "P")
