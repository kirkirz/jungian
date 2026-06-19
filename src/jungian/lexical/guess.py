"""Guess function usage by lexical analysis
It supports:
1) Phrase matching with weights
2) Word matching with weights
"""

import string


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


# This is a demo don't treat it seriously yet :D

LEXICON = {
    "logic": [("Ti", 2)],
    "analyze": [("Ti", 2)],
    "efficient": [("Te", 2)],
    "feel": [("Fi", 1), ("Fe", 1)],
    "maybe": [("Ne", 1)],
}

PHRASES = {
    "i think": [("Ti", 2)],
    "it depends": [("Ne", 2)],
    "on the other hand": [("Ne", 3)],
    "i feel like": [("Fi", 2), ("Fe", 1)],
}

scores = guess("I think this is logical.", LEXICON, PHRASES)
print(scores)
