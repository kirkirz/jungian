"""
Gut's encoding
Source:
https://web.archive.org/web/20020615231104/https://ru.laser.ru/authors/ss/gut/formalization.htm
"""

from jungian.function import Ne, Ni, Se, Si, Te, Ti, Fe, Fi
from jungian.type import (
    ENTp,
    ISFp,
    ESFj,
    INTj,
    ENFj,
    ISTj,
    ESTp,
    INFp,
    ESFp,
    INTp,
    ENTj,
    ISFj,
    ESTj,
    INFj,
    ENFp,
    ISTp,
)
from jungian.models.socionics.itr import (
    identical,
    mirror,
    activity,
    conflict,
    superego,
    dual,
    contrary,
    quasi_identity,
    kindred,
    business,
    semidual,
    illusionary,
    benefactor,
    beneficiary,
    supervisor,
    supervisee,
)

# IMEs (Introverted/Extraverted, Static/Dynamic, Internal/External)
IME_TO_GUT = {
    Ne: (-1, -1, -1),
    Ni: (1, 1, -1),
    Se: (-1, -1, 1),
    Si: (1, 1, 1),
    Te: (-1, 1, 1),
    Ti: (1, -1, 1),
    Fe: (-1, 1, -1),
    Fi: (1, -1, -1),
}

GUT_TO_IME = {v: k for k, v in IME_TO_GUT.items()}

RELATION_TO_GUT = {
    identical: (
        (1, 0, 0, 0),
        (0, 1, 0, 0),
        (0, 0, 1, 0),
        (0, 0, 0, 1),
    ),
    mirror: (
        (-1, 0, 0, 0),
        (0, 1, 0, 0),
        (0, 0, 0, 1),
        (0, 0, 1, 0),
    ),
    activity: (
        (1, 0, 0, 0),
        (0, -1, 0, 0),
        (0, 0, 0, -1),
        (0, 0, -1, 0),
    ),
    conflict: (
        (-1, 0, 0, 0),
        (0, 1, 0, 0),
        (0, 0, 0, -1),
        (0, 0, -1, 0),
    ),
    superego: (
        (1, 0, 0, 0),
        (0, 1, 0, 0),
        (0, 0, -1, 0),
        (0, 0, 0, -1),
    ),
    dual: (
        (-1, 0, 0, 0),
        (0, -1, 0, 0),
        (0, 0, -1, 0),
        (0, 0, 0, -1),
    ),
    contrary: (
        (-1, 0, 0, 0),
        (0, -1, 0, 0),
        (0, 0, 1, 0),
        (0, 0, 0, 1),
    ),
    quasi_identity: (
        (1, 0, 0, 0),
        (0, -1, 0, 0),
        (0, 0, 0, 1),
        (0, 0, 1, 0),
    ),
    kindred: (
        (1, 0, 0, 0),
        (0, 1, 0, 0),
        (0, 0, 1, 0),
        (0, 0, 0, -1),
    ),
    business: (
        (1, 0, 0, 0),
        (0, 1, 0, 0),
        (0, 0, -1, 0),
        (0, 0, 0, 1),
    ),
    semidual: (
        (-1, 0, 0, 0),
        (0, -1, 0, 0),
        (0, 0, -1, 0),
        (0, 0, 0, 1),
    ),
    illusionary: (
        (-1, 0, 0, 0),
        (0, -1, 0, 0),
        (0, 0, 1, 0),
        (0, 0, 0, -1),
    ),
    beneficiary: (
        (1, 0, 0, 0),
        (0, -1, 0, 0),
        (0, 0, 0, 1),
        (0, 0, -1, 0),
    ),
    benefactor: (
        (1, 0, 0, 0),
        (0, -1, 0, 0),
        (0, 0, 0, -1),
        (0, 0, 1, 0),
    ),
    supervisee: (
        (-1, 0, 0, 0),
        (0, 1, 0, 0),
        (0, 0, 0, -1),
        (0, 0, 1, 0),
    ),
    supervisor: (
        (-1, 0, 0, 0),
        (0, 1, 0, 0),
        (0, 0, 0, 1),
        (0, 0, -1, 0),
    ),
}

GUT_TYPES = {
    ENTp: (-1, -1, -1, 1),
    ISFp: (1, 1, 1, -1),
    ESFj: (-1, 1, -1, 1),
    INTj: (1, -1, 1, -1),
    ENFj: (-1, 1, -1, -1),
    ISTj: (1, -1, 1, 1),
    ESTp: (-1, -1, 1, 1),
    INFp: (1, 1, -1, -1),
    ESFp: (-1, -1, 1, -1),
    INTp: (1, 1, -1, 1),
    ENTj: (-1, 1, 1, -1),
    ISFj: (1, -1, -1, 1),
    ESTj: (-1, 1, 1, 1),
    INFj: (1, -1, -1, -1),
    ENFp: (-1, -1, -1, -1),
    ISTp: (1, 1, 1, 1),
}
