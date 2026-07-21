#!/usr/bin/env python3
"""Complete validation of Gut's encoding against functional intertype relations."""

import sys
from pathlib import Path

# Add src/ to Python path (works from repo root or examples/)
repo_root = Path(__file__).parent.parent
src_path = repo_root / "src"
sys.path.insert(0, str(src_path))

from jungian.type import (
    ENTp,
    INTp,
    ENFp,
    INFp,
    ESTp,
    ISTp,
    ESFp,
    ISFp,
    ENTj,
    INTj,
    ENFj,
    INFj,
    ESTj,
    ISTj,
    ESFj,
    ISFj,
    Type,
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
from jungian.models.socionics.gut import GUT_TYPES, RELATION_TO_GUT


# ---- Helper: apply Gut matrix ----
def vector_to_type(vec: tuple[int, int, int, int]) -> Type:
    """Convert a Gut 4-vector back to a Jungian Type."""
    for t, v in GUT_TYPES.items():
        if v == vec:
            return t
    raise ValueError(f"Vector {vec} does not match any known type")


def apply_relation(t: Type, relation_func) -> Type:
    """
    Apply a Gut relation matrix to a type's vector (row-vector multiplication).
    result[i] = sum_j vec[j] * matrix[j][i]
    """
    vec = GUT_TYPES[t]
    matrix = RELATION_TO_GUT[relation_func]

    # fmt: off
    result = (
        vec[0]*matrix[0][0] + vec[1]*matrix[1][0] + vec[2]*matrix[2][0] + vec[3]*matrix[3][0],
        vec[0]*matrix[0][1] + vec[1]*matrix[1][1] + vec[2]*matrix[2][1] + vec[3]*matrix[3][1],
        vec[0]*matrix[0][2] + vec[1]*matrix[1][2] + vec[2]*matrix[2][2] + vec[3]*matrix[3][2],
        vec[0]*matrix[0][3] + vec[1]*matrix[1][3] + vec[2]*matrix[2][3] + vec[3]*matrix[3][3],
    )
    # fmt: on
    return vector_to_type(result)


# ---- All 16 types ----
ALL_TYPES = [
    ENTp,
    INTp,
    ENFp,
    INFp,
    ESTp,
    ISTp,
    ESFp,
    ISFp,
    ENTj,
    INTj,
    ENFj,
    INFj,
    ESTj,
    ISTj,
    ESFj,
    ISFj,
]

# ---- All 16 relations ----
ALL_RELATIONS = [
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
]


def main():
    print("=" * 70)
    print("Gut Encoding Validation Suite")
    print("=" * 70)

    failures = []
    total_checks = 0

    for t in ALL_TYPES:
        for rel in ALL_RELATIONS:
            total_checks += 1
            try:
                gut_result = apply_relation(t, rel)
                func_result = rel(t)
                if gut_result != func_result:
                    failures.append((t, rel.__name__, gut_result, func_result))
            except Exception as e:
                failures.append((t, rel.__name__, f"ERROR: {e}", None))

    # ---- Summary ----
    print(f"\nTotal checks: {total_checks}")
    print(f"Failures:     {len(failures)}")

    if failures:
        print("\n❌ FAILURES:")
        for t, rel_name, gut_res, func_res in failures:
            print(f"  {t} {rel_name} -> Gut: {gut_res}, Func: {func_res}")
        raise AssertionError(f"{len(failures)} validation failures occurred.")
    else:
        print("\n✅ ALL TESTS PASSED!")
        print("Gut matrices perfectly match the functional intertype relations.")


if __name__ == "__main__":
    main()
