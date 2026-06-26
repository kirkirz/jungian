from jungian import Type, Function, switch_attitude, switch_process, to_dom_aux


def grant_stack(t: Type) -> tuple[Function, Function, Function, Function]:
    """Return the Grant stack"""
    dom, aux = to_dom_aux(t)
    p1 = dom
    p2 = aux
    p3 = switch_attitude(switch_process(aux))
    p4 = switch_attitude(switch_process(dom))
    return (p1, p2, p3, p4)
