from ex1 import (
    HealingCreatureFactory,
    TransformCreatureFactory
)


def healing_factory(hel: HealingCreatureFactory) -> None:
    print("Testing Creature with healing capability")
    print(" base:")
    h1 = hel.create_base()
    print(h1.describe())
    print(h1.attack())
    print(h1.heal("itself"))
    print(" evolved:")
    h1 = hel.create_evolved()
    print(h1.describe())
    print(h1.attack())
    print(h1.heal("itself"))


def transforming_factory(transf: TransformCreatureFactory) -> None:
    print("Testing Creature with transform capability")
    print(" base:")
    tr = transf.create_base()
    print(tr.describe())
    print(tr.attack())
    print(tr.transform())
    print(tr.attack())
    print(tr.revert())
    print(" evolved:")
    tr = transf.create_evolved()
    print(tr.describe())
    print(tr.attack())
    print(tr.transform())
    print(tr.attack())
    print(tr.revert())

if __name__ == "__main__":
    hel = HealingCreatureFactory()
    transform = TransformCreatureFactory()
    healing_factory(hel)
    print()
    transforming_factory(transform)
