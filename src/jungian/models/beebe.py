from jungian import Type, Function, switch_attitude, switch_process, to_dom_aux

def beebe_stack(t: Type) -> tuple[Function, Function, Function, Function]:
    """ Return the Beebe stack"""
    dom, aux = to_dom_aux(t)
    p1 = dom
    p2 = aux
    p3 = switch_attitude(switch_process(aux))
    p4 = switch_attitude(switch_process(dom))
    # Shadow:
    p5 = switch_attitude(p1)
    p6 = switch_attitude(p2)
    p7 = switch_attitude(p3)
    p8 = switch_attitude(p4)
    return (p1, p2, p3, p4, p5, p6, p7, p8)
