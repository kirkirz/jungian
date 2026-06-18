from jungian import Type, Function, switch_attitude, switch_process, to_dom_aux

def model_j_stack(t: Type) -> tuple[Function, Function, Function, Function]:
    """ Return the Model J stack"""
    dom, aux = to_dom_aux(t)
    p1 = dom
    p2 = aux
    p4 = switch_process(aux)
    p5 = switch_attitude(switch_process(dom))
    return (p1, p2, p4, p5)
