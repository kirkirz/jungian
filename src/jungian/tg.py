# src/jungian/lexical/guess.py

import json
import string
from pathlib import Path
from typing import Optional

def guess(text: str, lexicon: dict, phrases: dict) -> dict[str, int]:
    """The function to guess function usage"""
    _scores = {name: 0 for name in ["Ti", "Te", "Fi", "Fe", "Ni", "Ne", "Si", "Se"]}
    text_lower = text.lower()

    # 1. Phrase matching
    for phrase, mappings in phrases.items():
        if phrase in text_lower:
            for item in mappings:
                if isinstance(item, tuple):
                    func, weight = item
                    _scores[func] += weight
                else:
                    _scores[item] += 1

    # 2. Word-level scoring
    translator = str.maketrans("", "", string.punctuation)
    for word in text_lower.split():
        clean_word = word.translate(translator)
        if clean_word in lexicon:
            for item in lexicon[clean_word]:
                if isinstance(item, tuple):
                    func, weight = item
                    _scores[func] += weight
                else:
                    _scores[item] += 1

    return {name: weight for name, weight in _scores.items() if weight > 0}


def load_lexicon(path: str | Path) -> dict:
    """Load a lexicon from a JSON file."""
    with open(path, 'r') as f:
        return json.load(f)


def load_phrases(path: str | Path) -> dict:
    """Load phrases from a JSON file."""
    with open(path, 'r') as f:
        return json.load(f)


def guess_from_file(text: str, lexicon_path: str | Path, phrases_path: str | Path) -> dict[str, int]:
    """Guess function usage from text using JSON files."""
    lexicon = load_lexicon(lexicon_path)
    phrases = load_phrases(phrases_path)
    return guess(text, lexicon, phrases)
