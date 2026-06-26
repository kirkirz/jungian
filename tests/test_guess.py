from pathlib import Path
from jungian.lexical.guess import guess_from_file


def test_lexical():
    project_root = Path(__file__).parent.parent
    lexicon_path = project_root / "src" / "jungian" / "lexical" / "lexicon.json"

    scores = guess_from_file("i think it depends", lexicon_path)
    print("Lexical scores:", scores)


if __name__ == "__main__":
    test_lexical()
