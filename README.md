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
**Models supported**: PSys, Big5, MBTI, Socionics (Models A, J)
## Psys
* Psys function vectors
## Big5 (aka OCEAN, CANOE and FFM)
* Big5 dimensional data structure
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

# Quickstart for typology enthusiasts
Check belonging to a type group:
```py
from jungian.dichotomy import Dichotomy, E, N, T, P, I, S, F, J
from jungian.type import ENTP, INTJ, ENFP

NT = N & T

NT(ENTP) # True
NT(INTJ) # True
NT(ENFP) # False
```

Calculate intertype relations:
```py
from jungian.type import LIE, ILE
from jungian.models.socionics.itr import relation

relation(LIE, ILE) # Quasi-identity
```

Work with stacks:
```py
from jungian.type import INTP
from jungian.models.beebe import nemesis
print(f"Nemesis of INTP: {nemesis(INTP)}")
```

# ROADMAP
## Improving the core engine
* Make types constructed from dichotomies
* Add dimensional data support (a separate Dimension class along Dichotomy). Potentially supporting dichotomy algebra via fuzzy logic
* Better stack tooling, including universal pos() function
## Improving model support
* Add Ring, Block and Axis classes
* Tooling for other frameworks like KTS, OPS, 16P NERIS etc (there's a lot of them and implementation should be trivial once Dichotomy is polished). 
* Improving the API for existing models
## PSys concepts
* Adding support for Phase, Mode and Stance as standalone objects
* Implementing simulations
## Side quests
* Improve testing (unit tests are necessary to ensure the correctness of derivations).
* Add more lexicon files to the repo (data is crucial here)
* Add/improve examples, improve documentation
* Lint/refactor the code and make types more rigorous (mypy), improving packaging/config
