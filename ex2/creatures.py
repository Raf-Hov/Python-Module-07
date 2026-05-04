from ex2.capabilities import (
    Creature,
    HealCapability,
    TransformCapability
)


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


class Sproutling(Creature, HealCapability):
    def __init__(self):
        self.name = __class__.__name__
        super().__init__(self.name, "Grass")

    def attack(self) -> str:
        return f"{self.name} uses Vine Whip!"

    def heal(self, target: str) -> str:
        return f"{self.name} heals {target} and others for a large amount"


class Bloomelle(Creature, HealCapability):
    def __init__(self):
        self.name = __class__.__name__
        super().__init__(self.name, "Grass/Fairy")

    def attack(self) -> str:
        return f"{self.name} uses Petal Dance!"

    def heal(self, target: str) -> str:
        return f"{self.name} heals {target} and others for a large amount"


class Shiftling(Creature, TransformCapability):
    def __init__(self):
        self.name = __class__.__name__
        self._is_tra = False
        super().__init__(self.name, "Normal")

    def attack(self) -> str:
        if not self._is_tra:
            return f"{self.name} attacks normally."
        return f"{self.name} performs a boosted strike!"

    def transform(self):
        self._is_tra = True
        return f"{self.name} shifts into a sharper form!"

    def revert(self):
        return f"{self.name} returns to normal."


class Morphagon(Creature, TransformCapability):
    def __init__(self):
        self.name = __class__.__name__
        self._is_tra = False
        super().__init__(self.name, "Normal/Dragon")

    def attack(self) -> str:
        if not self._is_tra:
            return f"{self.name} attacks normally."
        return f"{self.name} unleashes a devastating morph strike!"

    def transform(self):
        self._is_tra = True
        return f"{self.name} morphs into a dragonic battle form!"

    def revert(self):
        return f"{self.name} stabilizes its form."
