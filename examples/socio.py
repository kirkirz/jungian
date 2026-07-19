"""Socionics features demo."""

from jungian.type import ENTp, INTj
from jungian.function import Ti
from jungian.models.socionics.ModelA import model_a_stack, pos
from jungian.models.socionics.dimensionality import dim
from jungian.models.socionics.itr import relation, dual
from jungian.models.socionics.groups import (
    quadra,
    club,
    Aggressor,
    Caregiver,
    Childlike,
    Victim,
)
from jungian.models.socionics.sign import sign_wikisocion, sign_model_g


def main():
    print("------- Types/stacks --------")
    t = ENTp

    # Groups
    print(f"Quadra: {quadra(t)}")
    print(f"Club:   {club(t)}")
    print(
        f"Romance: {'Aggressor' if Aggressor(t) else 'Caregiver' if Caregiver(t) else 'Childlike' if Childlike(t) else 'Victim'}"
    )

    # ITRs
    print(f"Relation to INTj: {relation(t, INTj).__name__}")
    print(f"Duality partner:  {dual(t)}")
    print(f"Type: {t}")

    # Stack
    print("Model A stack:", " ".join(str(f) for f in model_a_stack(t)))

    print("--------- Functions --------")
    # Position and dimensionality
    position = pos(t, Ti)
    print(f"Ti is position {position} (dimensionality {dim(position)})")

    # Signs
    print(f"Wikisocion sign: {sign_wikisocion(t, Ti)}")
    print(f"Model G sign:    {sign_model_g(t, Ti)}")


if __name__ == "__main__":
    main()
