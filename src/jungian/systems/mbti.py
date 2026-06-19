"""MBTI type codes"""

from jungian import Type

# Mapping from MBTI code to canonical Type
# It does so-called J/P switch
# That means that rational introverts (j) are perceivers (P)
# and irrational introverts (p) are judgers (J)
MBTI_MAP = {
    "ENTP": Type("E", "N", "T", "p"),
    "INTP": Type("I", "N", "T", "j"),
    "ENTJ": Type("E", "N", "T", "j"),
    "INTJ": Type("I", "N", "T", "p"),
    "ENFP": Type("E", "N", "F", "p"),
    "INFP": Type("I", "N", "F", "j"),
    "ENFJ": Type("E", "N", "F", "j"),
    "INFJ": Type("I", "N", "F", "p"),
    "ESTP": Type("E", "S", "T", "p"),
    "ISTP": Type("I", "S", "T", "j"),
    "ESTJ": Type("E", "S", "T", "j"),
    "ISTJ": Type("I", "S", "T", "p"),
    "ESFP": Type("E", "S", "F", "p"),
    "ISFP": Type("I", "S", "F", "j"),
    "ESFJ": Type("E", "S", "F", "j"),
    "ISFJ": Type("I", "S", "F", "p"),
}


def from_mbti(code: str) -> Type:
    """Convert an MBTI code (e.g., 'ENTP') to a canonical Type."""
    return MBTI_MAP[code.upper()]


def to_mbti(t: Type) -> str:
    """Convert a canonical Type to an MBTI code."""
    # Reverse lookup
    for code, typ in MBTI_MAP.items():
        if typ == t:
            return code
    raise ValueError(f"Type {t} not found in MBTI mapping")
