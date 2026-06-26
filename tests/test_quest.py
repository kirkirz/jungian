# tests/test_quest.py

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from jungian.questionnaires.quest import load_quest, score_quest, normalize_scores


def test_quest():
    # Get the project root
    project_root = Path(__file__).parent.parent

    # Samples are inside the package
    sample_path = (
        project_root
        / "src"
        / "jungian"
        / "questionnaires"
        / "samples"
        / "functional.json"
    )

    data = load_quest(sample_path)
    answers = [3, 4, 2, 3, 4, 2, 3, 4, 2, 3, 4, 2, 3, 4, 2, 3, 4, 2, 3, 4, 2, 3, 4, 2]
    raw = score_quest(data, answers)
    norm = normalize_scores(raw, data)

    print("Raw:", raw)
    print("Normalized:", norm)
    print("All tests passed!")


if __name__ == "__main__":
    test_quest()
