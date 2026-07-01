Jungian.py, a theory-agnostic Python library for working with Jungian typology).

Official repo:
https://github.com/kirkirz/jungian

[![PyPI version](https://badge.fury.io/py/jungian.svg)](https://badge.fury.io/py/jungian)
It's available on PyPI:  
`pip install jungian`

This was initially built for my own system (PSys), but we will gladly support other systems.  
It is intended as the most comprehensive library, that anyone could use, no matter what system they support, so that we would benefit from common infrastructure.

Contributions are very welcome.
# Planned structure
`src/systems/`: Separate standalone systems

`src/models/` : Models for systems, that exist

`src/lexical/` : Lexical analysis tooling  

`src/questionnaires/` : Questionnaires tooling

`src/simulations/` : Simulations for cognitive functions

# Models vs systems
To make the library less messy, we separate systems (ontologies) and models (lenses).

A system is a complete theory of typology (e.g., MBTI, Socionics, PSys), with its own ontology and rules.

A model is a specific way of interpreting existing systems (Grant/Beebe stacks, 16P NERIS, Model A, Model J).

All socionics-related stuff should live inside `src/systems/socionics/` and `src/models/socionics/`
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
* Intertype relations (implemented 12/14)
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
