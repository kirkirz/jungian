from jungian.type import Type
from jungian.function import Function, Te, Ti, Fe, Fi
from jungian.models.socionics.ModelA import pos
from jungian.systems.socionics.reinin import is_democratic, is_positivist


def sign_wikisocion(t: Type, f: Function) -> str:
    """Sign as defined in wikisocion"""
    is_rational = f in [Te, Ti, Fe, Fi]

    if is_democratic(t):
        # Irrational +, Rational -
        return "+" if not is_rational else "-"
    # Irrational -, Rational +
    return "-" if not is_rational else "+"


def sign_model_g(t: Type, f: Function) -> str:
    """
    Return the Model G sign for a function.

    Rule:
    - Positivist: Mental (1-4) = '+', Vital (5-8) = '-'
    - Negativist: Mental (1-4) = '-', Vital (5-8) = '+'
    """
    position = pos(t, f)
    is_mental = position <= 4
    if is_positivist(t):
        return "+" if is_mental else "-"
    return "-" if is_mental else "+"
