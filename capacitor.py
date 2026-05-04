from ex1 import (
    HealingCreatureFactory,
    TransformCreatureFactory
)


def healing_factory(hel: HealingCreatureFactory) -> None:
    print("Testing Creature with healing capability")
    print(" base:")
    healer1 = hel.create_base()
    print(healer1.describe())
    print(healer1.attack())
    print(healer1.heal("itself"))
    print(" evolved:")
    healer2 = hel.create_evolved()
    print(healer2.describe())
    print(healer2.attack())
    print(healer2.heal("itself"))


def transforming_factory(transf: TransformCreatureFactory) -> None:
    print("Testing Creature with transform capability")
    print(" base:")
    tf1 = transf.create_base()
    print(tf1.describe())
    print(tf1.attack())
    print(tf1.transform())
    print(tf1.attack())
    print(tf1.revert())
    print(" evolved:")
    tf2 = transf.create_evolved()
    print(tf2.describe())
    print(tf2.attack())
    print(tf2.transform())
    print(tf2.attack())
    print(tf2.revert())


if __name__ == "__main__":
    hel = HealingCreatureFactory()
    transform = TransformCreatureFactory()
    healing_factory(hel)
    print()
    transforming_factory(transform)
