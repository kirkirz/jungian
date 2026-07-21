"""Test the identical relation for all 16 types."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

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
)
from jungian.models.socionics.itr import identical, relation


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


def test_identical():
    """Test that every type is identical to itself."""
    print("Testing identical relation...\n")
    passed = 0
    failed = 0

    for t in ALL_TYPES:
        result = relation(t, t)
        if result is identical:
            print(f"  ✅ {t} → {t}: identical")
            passed += 1
        else:
            print(f"  ❌ {t} → {t}: got {result.__name__}, expected identical")
            failed += 1

    print(f"\n{'='*50}")
    print(f"Passed: {passed}/{len(ALL_TYPES)}")
    print(f"Failed: {failed}/{len(ALL_TYPES)}")

    assert failed == 0, f"{failed} tests failed"


if __name__ == "__main__":
    test_identical()
