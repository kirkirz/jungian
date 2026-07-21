"""Classical intertype relations from socionics"""

from functools import lru_cache
from typing import Callable
from jungian import Type, to_dom_aux, from_dom_aux, switch_process, switch_attitude

Relation = Callable[[Type], Type]


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


def benefactor(t: Type) -> Type:
    """Benefactor relation: 1→8, 2→5. Returns the benefactor"""
    dom, aux = to_dom_aux(t)
    new_dom = switch_attitude(aux)  # position 8
    new_aux = switch_attitude(switch_process(dom))  # position 5
    return from_dom_aux(new_dom, new_aux)


def beneficiary(t: Type) -> Type:
    """Beneficiary relation: 1→6, 2→7. Returns the beneficiary"""
    dom, aux = to_dom_aux(t)
    new_dom = switch_attitude(switch_process(aux))  # position 6
    new_aux = switch_attitude(dom)  # position 7
    return from_dom_aux(new_dom, new_aux)


def supervisor(t: Type) -> Type:
    """Supervisor relation: 1→4, 2→1. Returns the supervisor"""
    dom, aux = to_dom_aux(t)
    new_dom = switch_process(aux)  # position 4
    new_aux = dom  # position 1
    return from_dom_aux(new_dom, new_aux)


def supervisee(t: Type) -> Type:
    """Supervisee relation: 1→2, 2→3. Returns the supervisee"""
    dom, aux = to_dom_aux(t)
    new_dom = aux  # position 2
    new_aux = switch_process(dom)  # position 3
    return from_dom_aux(new_dom, new_aux)


RELATIONS = (
    identical,
    mirror,
    conflict,
    dual,
    kindred,
    semidual,
    business,
    illusionary,
    quasi_identity,
    contrary,
    superego,
    activity,
    benefactor,
    beneficiary,
    supervisor,
    supervisee,
)


def relate(registry: tuple[Relation, ...]):
    """Factory that returns a memoized dispatcher for intertype relations."""

    @lru_cache
    def lookup(t1: Type, t2: Type) -> Relation:
        for rel in registry:
            if rel(t1) == t2:
                return rel
        raise LookupError(f"No relation found between {t1} and {t2}")

    return lookup


relation = relate(RELATIONS)
