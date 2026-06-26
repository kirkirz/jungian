from jungian import Type, Function, switch_attitude, switch_process, to_dom_aux


def model_a_stack(
    t: Type,
) -> tuple[
    Function, Function, Function, Function, Function, Function, Function, Function
]:
    """Return the classical Model A stack"""
    dom, aux = to_dom_aux(t)
    p1 = dom
    p2 = aux
    p3 = switch_process(dom)
    p4 = switch_process(aux)
    p5 = switch_attitude(switch_process(dom))
    p6 = switch_attitude(switch_process(aux))
    p7 = switch_attitude(dom)
    p8 = switch_attitude(aux)
    return (p1, p2, p3, p4, p5, p6, p7, p8)


def pos(t: Type, f: str | Function) -> int:
    stack = model_a_stack(t)
    return next(
        i
        for i, fn in enumerate(stack, start=1)
        if repr(fn) == (f if isinstance(f, str) else repr(f))
    )
