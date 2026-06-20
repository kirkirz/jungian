Jungian.py, a theory-agnostic Python library for working with Jungian typology).

It's available on PyPI (although without latest features):  
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
* Reinin dichotomies (3/11 implemented, contributions are welcome!)
* Model A, Model J stacks
* Function signing (legacy and modern systems)
* Intertype relations (implemented 9/14)
* Dimensionality
