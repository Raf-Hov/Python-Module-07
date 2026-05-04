from .creatures import (
    Flameling,
    Aquabub,
    Sproutling,
    Bloomelle,
    Shiftling,
    Morphagon,
    Torragon,
    Pyrodon,
)
from .capabilities import CreatureFactory


class FlameFactory(CreatureFactory):
    def __init__(self):
        self.name = __class__.__name__
        self.new_name = self.name.replace(self.name, "Flame")
        super().__init__(self.new_name)

    def create_base(self) -> Flameling:
        return Flameling()

    def create_evolved(self) -> Pyrodon:
        return Pyrodon()


class AquaFactory(CreatureFactory):
    def __init__(self):
        self.name = __class__.__name__
        self.new_name = self.name.replace(self.name, "Aqua")
        super().__init__(self.new_name)

    def create_base(self) -> Aquabub:
        return Aquabub()

    def create_evolved(self) -> Torragon:
        return Torragon()


class HealingCreatureFactory(CreatureFactory):
    def __init__(self):
        self.name = __class__.__name__
        self.new_name = self.name.replace(self.name, "Healing")
        super().__init__(self.new_name)

    def create_base(self) -> Sproutling:
        return Sproutling()

    def create_evolved(self) -> Bloomelle:
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):
    def __init__(self):
        self.name = __class__.__name__
        self.new_name = self.name.replace(self.name, "Transform")
        super().__init__(self.new_name)

    def create_base(self) -> Shiftling:
        return Shiftling()

    def create_evolved(self) -> Morphagon:
        return Morphagon()
