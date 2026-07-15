"""Command Line Interface to execute inventories and generate FHIR outputs."""

import argparse
import json
from pathlib import Path
from .quest import load_quest, score_quest, normalize_scores, get_scale_config
from .quest_fhir import questionnaire_to_fhir, response_to_fhir

DEFAULT_URL = "http://example.org"


def _prompt_answers(data: dict, min_val: int, max_val: int) -> list[int]:
    """Interactively collect valid numeric responses from the user."""
    answers = []
    for i, item in enumerate(data["items"], 1):
        text = item["text"]
        reverse = " (R)" if item.get("reverse", False) else ""

        while True:
            try:
                user_input = input(f"{i:2}. {text}{reverse} [{min_val}-{max_val}]: ")
                stripped_input = user_input.strip()
                if stripped_input == "":
                    continue
                val_int = int(stripped_input)
                if min_val <= val_int <= max_val:
                    answers.append(val_int)
                    break
                print(f"  Please enter a number between {min_val} and {max_val}.")
            except ValueError:
                print("  Please enter a valid integer.")
    return answers


def _render_results(norm: dict[str, float]) -> None:
    """Print the normalized scoring output to the console."""
    print("\n" + "=" * 50)
    print("📊 RAW SCORES\n")

    sorted_scores = sorted(norm.items(), key=lambda x: -x[1])
    for key, score in sorted_scores:
        visual_bar = "█" * int(score // 10) + "░" * int(10 - score // 10)
        print(f"  {key}: {score:5.1f}% {visual_bar}")

    print("\n" + "-" * 50)
    print("JSON OUTPUT:")
    print(json.dumps(norm, indent=2))


def run_quest(
    quest_path: Path, export_fhir: bool = False, base_domain: str = DEFAULT_URL
) -> None:
    """Run a questionnaire in the terminal with dynamic scale bounds."""
    if not quest_path.exists():
        print(f"❌ Error: Questionnaire file not found at '{quest_path}'")
        return

    data = load_quest(quest_path)
    scale = get_scale_config(data)
    min_val, max_val, labels = scale["min"], scale["max"], scale["labels"]

    print(f"\n📋 {data['name']}\n")
    print(f"Answer each question on a scale of {min_val}-{max_val}:")
    for val, label in zip(range(min_val, max_val + 1), labels):
        print(f"  {val} = {label}")
    print()

    answers = _prompt_answers(data, min_val, max_val)
    norm = normalize_scores(score_quest(data, answers), data)

    _render_results(norm)

    if export_fhir:
        fhir_template = questionnaire_to_fhir(data, base_domain=base_domain)
        fhir_submission = response_to_fhir(data, answers, norm, base_domain=base_domain)

        Path("fhir_questionnaire.json").write_text(
            json.dumps(fhir_template, indent=2), encoding="utf-8"
        )
        Path("fhir_response.json").write_text(
            json.dumps(fhir_submission, indent=2), encoding="utf-8"
        )
        print(f"\n💾 Saved FHIR schemas using domain [{base_domain}]")
        print("   -> fhir_questionnaire.json")
        print("   -> fhir_response.json")

    print("\n" + "=" * 50)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=(
            "Run a psychometric inventory in your terminal and optionally "
            "export standard FHIR medical formats."
        )
    )

    parser.add_argument(
        "file",
        type=Path,
        help="Path to your inventory JSON file.",
    )
    parser.add_argument(
        "--fhir",
        action="store_true",
        help="Compile and export FHIR Questionnaire and QuestionnaireResponse schemas.",
    )
    parser.add_argument(
        "--domain",
        type=str,
        default=DEFAULT_URL,
        help="Custom base URI/domain string for the FHIR resource namespace identifiers.",
    )

    args = parser.parse_args()
    run_quest(
        quest_path=args.file, export_fhir=args.fhir, base_domain=args.domain
    )
