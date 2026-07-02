Jungian.py, a theory-agnostic Python library for working with Jungian typology.

Official repo:
https://github.com/kirkirz/jungian

[![PyPI version](https://badge.fury.io/py/jungian.svg)](https://badge.fury.io/py/jungian)
It's available on PyPI:  
`pip install jungian`

This was initially built for my own system (PSys), but we will gladly support other systems.  
It is intended as the most comprehensive library, that anyone could use, no matter what system they support, so that we would benefit from common infrastructure.

Contributions are very welcome.
# Planned structure
`src/models/` : Typology model catalogue

`src/lexical/` : Lexical analysis tooling  

`src/questionnaires/` : Questionnaires tooling

Simulations will live inside `src/models/psys/`
# Features
**Systems supported**: 3  
**Models supported**: 4
## Psys
* Psys function vectors
## MBTI
* Beebe and Grant stacks
* MBTI type codes
## Socionics
* Reinin dichotomies
* Model A, Model J stacks
* Function signing (legacy and modern systems)
* All 14 classical intertype relations
* Dimensionality
* Small groups
# Lexical analysis
* supports custom lexicon files
* multiple weighted functions per token
* phrase handling (supports fuzzy detection) and punctuation handling
# Questionnaire engine
* weighted questions with variants
* supports both dichotomy-typing and function-typing through a unified mapping system, custom flexible JSON DSL (+ config-driven scoring interpreter for trait-based models)
* CLI runner to use it interactively
* Likert scoring + normalisation of scores, reverse scoring
