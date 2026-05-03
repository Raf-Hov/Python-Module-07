from ex0 import FlameFactory, AquaFactory


def test_factorys(flame: FlameFactory, aqua: AquaFactory) -> None:
    print("Testing factory")
    f1 = flame.create_base()
    f2 = flame.create_evolved()
    print(f"{f1.describe()}\n{f1.attack()}")
    print(f"{f2.describe()}\n{f2.attack()}")
    print("\nTesting factory")
    f1 = aqua.create_base()
    f2 = aqua.create_evolved()
    print(f"{f1.describe()}\n{f1.attack()}")
    print(f"{f2.describe()}\n{f2.attack()}")


def fight(flame: FlameFactory, aqua: AquaFactory) -> None:
    print("\nTesting battle")
    f1 = flame.create_base()
    f2 = aqua.create_base()
    print(f"{f1.describe()}\n vs.\n{f2.describe()}\n fight!")
    print(f1.attack())
    print(f2.attack())


if __name__ == "__main__":
    flame = FlameFactory()
    aqua = AquaFactory()
    test_factorys(flame, aqua)
    fight(flame, aqua)
