"""Classical intertype relations from socionics"""

from jungian import Type, to_dom_aux, from_dom_aux, switch_process, switch_attitude


def identical(ty: Type) -> Type:
    """Identical relation"""
    return ty


def mirror(t: Type) -> Type:
    """Mirror relation: swap dominant/auxiliary."""
    dom, aux = to_dom_aux(t)
    return from_dom_aux(aux, dom)


def conflict(t: Type) -> Type:
    """Conflict relation: 1<->4, 2<->3."""
    dom, aux = to_dom_aux(t)
    return from_dom_aux(switch_process(aux), switch_process(dom))


def dual(t: Type) -> Type:
    """Duality relation: 1<->5, 2<->6, 3<->7, 4<->8."""
    dom, aux = to_dom_aux(t)
    new_dom = switch_attitude(switch_process(dom))
    new_aux = switch_attitude(switch_process(aux))
    return from_dom_aux(new_dom, new_aux)


def kindred(t: Type) -> Type:
    """Kindred relation"""
    dom, aux = to_dom_aux(t)
    new_aux = switch_process(aux)
    return from_dom_aux(dom, new_aux)


def semidual(t: Type) -> Type:
    """Semidual relation"""
    dom, aux = to_dom_aux(t)
    new_dom = switch_process(switch_attitude(dom))
    new_aux = switch_attitude(aux)
    return from_dom_aux(new_dom, new_aux)


def business(t: Type) -> Type:
    """Business relation"""
    dom, aux = to_dom_aux(t)
    new_dom = switch_process(dom)
    return from_dom_aux(new_dom, aux)


def illusionary(t: Type) -> Type:
    dom, aux = to_dom_aux(t)
    new_dom = switch_attitude(dom)
    new_aux = switch_process(switch_attitude(aux))
    return from_dom_aux(new_dom, new_aux)


def quasi_identity(t: Type) -> Type:
    dom, aux = to_dom_aux(t)
    new_dom = switch_attitude(aux)
    new_aux = switch_attitude(dom)
    return from_dom_aux(new_dom, new_aux)


def contrary(t: Type) -> Type:
    """Contrary relation"""
    dom, aux = to_dom_aux(t)
    new_dom = switch_attitude(dom)
    new_aux = switch_attitude(aux)
    return from_dom_aux(new_dom, new_aux)


def superego(t: Type) -> Type:
    """Super-ego relation: 1<->3, 2<->4"""
    dom, aux = to_dom_aux(t)
    new_dom = switch_process(dom)
    new_aux = switch_process(aux)
    return from_dom_aux(new_dom, new_aux)


def activity(t: Type) -> Type:
    """Activity relation"""
    dom, aux = to_dom_aux(t)
    new_dom = switch_attitude(switch_process(aux))
    new_aux = switch_attitude(switch_process(dom))
    return from_dom_aux(new_dom, new_aux)


def relation(t1: Type, t2: Type):
    """Return the intertype relation name between two types."""

    if t1 == t2:
        return identical
    if mirror(t1) == t2:
        return mirror
    if conflict(t1) == t2:
        return conflict
    if dual(t1) == t2:
        return dual
    if kindred(t1) == t2:
        return kindred
    if semidual(t1) == t2:
        return semidual
    if business(t1) == t2:
        return business
    if illusionary(t1) == t2:
        return illusionary
    if quasi_identity(t1) == t2:
        return quasi_identity
    if contrary(t1) == t2:
        return contrary
    if superego(t1) == t2:
        return superego
    if activity(t1) == t2:
        return activity

    raise ValueError(f"No relation found between {t1} and {t2}")
