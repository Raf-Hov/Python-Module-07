from .capabilities import (
    BattleStrategy,
    Creature,
    TransformCapability,
    HealCapability
)


class NormalStrategy(BattleStrategy):
    def __init__(self):
        self.name = __class__.__name__
        self.new_name = self.name.replace(self.name, "Normal")
        super().__init__(self.new_name)

    def act(self, creature: Creature) -> str:
        h1 = "Battle error, aborting tournament:  Invalid Creature"
        if isinstance(creature, TransformCapability):
            h3 = f"for this {self.name.lower()} strategy"
            return f"{h1} '{creature.name}' {h3}"
        return creature.attack()

    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, Creature):
            return True
        return False


class DefensiveStrategy(BattleStrategy):
    def __init__(self):
        self.name = __class__.__name__
        self.new_name = self.name.replace(self.name, "Defensive")
        super().__init__(self.new_name)

    def act(self, creature: Creature) -> str:
        h2 = "Battle error, aborting tournament:  Invalid Creature"
        if not isinstance(creature, HealCapability):
            h3 = f"for this {self.name.lower()} strategy"
            return f"{h2} {creature.name} {h3}"
        return f"{creature.attack()}\n{creature.heal('itself')}"

    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, HealCapability):
            return True
        return False


class AggressiveStrategy(BattleStrategy):
    def __init__(self):
        self.name = __class__.__name__
        self.new_name = self.name.replace(self.name, "Aggressive")
        super().__init__(self.new_name)

    def act(self, creature: Creature) -> str:
        h2 = "Battle error, aborting tournament: Invalid Creature"
        if not isinstance(creature, TransformCapability):
            h3 = f"for this {self.name.lower()} strategy"
            return f"{h2} {creature.name} {h3}"
        h1 = creature.revert()
        return f"{creature.transform()}\n{creature.attack()}\n{h1}"

    def is_valid(self, creature: Creature):
        if isinstance(creature, TransformCapability):
            return True
        return False
