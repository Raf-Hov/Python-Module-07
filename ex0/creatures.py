from abc import ABC, abstractmethod
# from typing import TypeVar, Generic


class Creature(ABC):
    def __init__(self, name: str, type: str):
        self.name: str = name.capitalize()
        self.type: str = type

    @abstractmethod
    def attack() -> str:
        pass

    def describe(self) -> str:
        return f"{self.name} is a {self.type} type Creature"


class Flameling(Creature):
    def __init__(self):
        self.name = __class__.__name__
        self.type("Fire")
        super().__init__(self.name, self.type)

    def attack(self) -> str:
        return "Flameling uses Ember!"


class Pyrodon(Creature):
    def __init__(self):
        self.name = __class__.__name__
        self.type("Fire/Flying")
        super().__init__(self.name, self.type)

    def attack(self) -> str:
        return "Flameling uses Flamethrower!"


class Aquabub(Creature):
    def __init__(self):
        self.name = __class__.__name__
        self.type("Water")
        super().__init__(self.name, self.type)

    def attack(self) -> str:
        return "Flameling uses Gun!"


class Torragon(Creature):
    def __init__(self):
        self.name = __class__.__name__
        self.type("Water")
        super().__init__(self.name, self.type)

    def attack(self) -> str:
        return "Flameling uses Pump!"


class CreatureFactory(ABC):
    @abstractmethod
    def create_base() -> None:
        pass

    @abstractmethod
    def create_evolved():
        pass


class FlameFactory(CreatureFactory):
    def __init__(self):
        print("Testing factory")
        self.fleam_list: list = []

    def create_base(self) -> None:
        flame1 = Flameling()
        flame2 = Pyrodon()
        self.flame_list = [flame1, flame2]

    def create_evolved(self) -> None:
        for i in self.flame_list:



class AquaFactory(CreatureFactory):
    pass


if __name__ == "__main__":
    pass
