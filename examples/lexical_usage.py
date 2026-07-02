"""Demonstrate the lexical analyzer with a sample text."""

import sys
from pathlib import Path

# Add src/ to Python path so jungian can be imported
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from jungian.lexical.guess import guess_from_file

lexicon_path = Path(__file__).parent.parent / "src" / "jungian" / "lexical" / "lexicon.json"

if __name__ == "__main__":
    text = "I think it depends on the situation, but I usually rely on logic and systems."
    scores = guess_from_file(text, lexicon_path)
    print(f"Input: {text}")
    print(f"Scores: {scores}")
