"""Demonstrate the lexical analyzer with a sample text."""

from pathlib import Path
from jungian.lexical.guess import guess_from_file

lexicon_path = (
    Path(__file__).parent.parent / "src" / "jungian" / "lexical" / "lexicon.json"
)

if __name__ == "__main__":
    TEXT = (
        "I think it depends on the situation, but I usually rely on logic and systems."
    )
    scores = guess_from_file(TEXT, lexicon_path)
    print(f"Input: {TEXT}")
    print(f"Scores: {scores}")
