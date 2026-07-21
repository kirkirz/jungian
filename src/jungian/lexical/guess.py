"""Lexical analyzer"""

import json
import string
from pathlib import Path
import re

FUNCTIONS = ["Ti", "Te", "Fi", "Fe", "Ni", "Ne", "Si", "Se"]


def normalize_items(items):
    """
    Accepts:
      - ["Ti", 2]  (JSON list form)
      - ("Ti", 2)  (tuple form if manually constructed)
      - "Ti"       (implicit weight 1)
    Returns: list[tuple(func, weight)]
    """
    out = []
    for item in items:
        if isinstance(item, (list, tuple)) and len(item) == 2:
            out.append((item[0], item[1]))
        else:
            out.append((item, 1))
    return out


def load_lexicon(path: str | Path) -> tuple[dict, dict]:
    """Load lexicon and phrases from JSON file."""
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    lexicon = {
        k.lower(): normalize_items(v) for k, v in data.get("lexicon", {}).items()
    }

    phrases = {
        k.lower(): normalize_items(v) for k, v in data.get("phrases", {}).items()
    }

    return lexicon, phrases


def guess(text: str, lexicon: dict, phrases: dict) -> dict[str, int]:
    """
    Hybrid heuristic scorer:
    - fuzzy phrase matching (substring-based, robust)
    - word-level lexicon scoring
    """
    scores = {f: 0 for f in FUNCTIONS}

    text_lower = text.lower()

    # single-pass punctuation cleanup
    translator = str.maketrans("", "", string.punctuation)
    clean_text = text_lower.translate(translator)

    # 1. Phrase matching (FIXED: fuzzy, no regex brittleness)
    for phrase, mappings in phrases.items():
        if re.search(r"\b" + re.escape(phrase) + r"\b", text_lower):
            boost = 1

            # optional reinforcement if punctuation doesn't break it
            if phrase in clean_text:
                boost += 1

            for func, weight in mappings:
                scores[func] += weight * boost

    # 2. Word-level scoring
    for word in clean_text.split():
        if word in lexicon:
            for func, weight in lexicon[word]:
                scores[func] += weight

    return {k: v for k, v in scores.items() if v > 0}


def guess_from_file(text: str, path: str | Path) -> dict[str, int]:
    """Guess from file"""
    lexicon, phrases = load_lexicon(path)
    return guess(text, lexicon, phrases)
