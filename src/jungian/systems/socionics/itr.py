"""Classical intertype relations from socionics"""
from jungian import Type, to_dom_aux, from_dom_aux

def identical(ty: Type) -> Type:
    """Identical relation"""
    return ty

def mirror(t: Type) -> Type:
    """Mirror relation: swap dominant/auxiliary."""
    dom, aux = to_dom_aux(t)
    return from_dom_aux(aux, dom)

def relation(t1: Type, t2: Type) -> str:
    """Return the intertype relation name between two types."""

    if t1 == t2:
        return identical
    if mirror(t1) == t2:
        return mirror
    raise ValueError(f"No relation found between {t1} and {t2}")
