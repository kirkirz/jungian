import sys
import json
from pathlib import Path
from quest import load_quest, score_quest, normalize_scores


def run_quest(quest_path: str):
    """Run a questionnaire in the terminal."""

    data = load_quest(quest_path)
    print(f"\n📋 {data['name']}\n")
    print("Answer each question on a scale of 0-4:")
    print("  0 = Strongly Disagree")
    print("  1 = Disagree")
    print("  2 = Neutral")
    print("  3 = Agree")
    print("  4 = Strongly Agree\n")

    answers = []
    for i, item in enumerate(data["items"], 1):
        text = item["text"]
        reverse = " (R)" if item.get("reverse", False) else ""

        while True:
            try:
                val = input(f"{i:2}. {text}{reverse} [0-4]: ")
                if val == "":
                    continue
                val = int(val)
                if 0 <= val <= 4:
                    answers.append(val)
                    break
                print("  Please enter a number between 0 and 4.")
            except ValueError:
                print("  Please enter a number.")

    raw = score_quest(data, answers)
    norm = normalize_scores(raw, data)

    print("\n" + "=" * 50)
    print("📊 RAW SCORES\n")

    sorted_scores = sorted(norm.items(), key=lambda x: -x[1])
    for key, score in sorted_scores:
        bar = "█" * int(score // 10) + "░" * int(10 - score // 10)
        print(f"  {key}: {score:5.1f}% {bar}")

    print("\n" + "-" * 50)
    print("JSON OUTPUT:")
    print(json.dumps(norm, indent=2))
    print("\n" + "=" * 50)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        run_quest(sys.argv[1])
    else:
        script_dir = Path(__file__).parent
        default_path = script_dir / "samples/functional.json"
        if default_path.exists():
            run_quest(str(default_path))
        else:
            print("Usage: python quest_cli.py <quest_file.json>")
            print("Example: python quest_cli.py functional.json")
