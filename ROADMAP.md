# Improving the core engine
* Make types constructed from dichotomies
* Add dimensional data support (a separate Dimension class along Dichotomy). Potentially supporting dichotomy algebra via fuzzy logic
* Better stack tooling, including universal pos() function
# Improving model support
* Add Ring, Block and Axis classes
* Tooling for other frameworks like KTS, OPS, 16P NERIS etc (there's a lot of them and implementation should be trivial once Dichotomy is polished). 
* Improving the API for existing models
# PSys concepts
* Adding support for Phase, Mode and Stance as standalone objects
* Implementing simulations
# Side quests
* Improve testing (unit tests are necessary to ensure the correctness of derivations).
* Add more lexicon files to the repo (data is crucial here)
* Add/improve examples, improve documentation
* Lint/refactor the code and make types more rigorous (mypy), improving packaging/config
