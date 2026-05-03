from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, type: str):
        self.name: str = name.capitalize()
        self.type: str = type

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return f"{self.name} is a {self.type} type Creature"


class Flameling(Creature):
    def __init__(self):
        self.name = __class__.__name__
        self.type = "Fire"
        super().__init__(self.name, self.type)

    def attack(self) -> str:
        return "Flameling uses Ember!"


class Pyrodon(Creature):
    def __init__(self):
        self.name = __class__.__name__
        self.type = "Fire/Flying"
        super().__init__(self.name, self.type)

    def attack(self) -> str:
        return "Pyrodon uses Flamethrower!"


class Aquabub(Creature):
    def __init__(self):
        self.name = __class__.__name__
        self.type = "Water"
        super().__init__(self.name, self.type)

    def attack(self) -> str:
        return "Aquabub uses Gun!"


class Torragon(Creature):
    def __init__(self):
        self.name = __class__.__name__
        self.type = "Water"
        super().__init__(self.name, self.type)

    def attack(self) -> str:
        return "Torragon uses Pump!"
