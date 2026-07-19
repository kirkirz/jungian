"""Demonstrate the questionnaire engine with a sample questionnaire."""

from pathlib import Path
from jungian.questionnaires.quest import load_quest, score_quest, normalize_scores


def main():
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


if __name__ == "__main__":
    main()
