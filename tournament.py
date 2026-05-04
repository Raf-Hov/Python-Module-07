from ex2 import (
    FlameFactory,
    HealingCreatureFactory,
    AggressiveStrategy,
    NormalStrategy,
    TransformCreatureFactory,
    AquaFactory,
    DefensiveStrategy,
    Creature,
    CreatureFactory,
    BattleStrategy
)


def batlle(str_list: list[str]) -> None:
    fact1 = HealingCreatureFactory()
    fact2 = FlameFactory()
    fact3 = TransformCreatureFactory()
    fact4 = AquaFactory()
    flame1 = fact2.create_base()
    flame2 = fact2.create_evolved()
    healing1 = fact1.create_base()
    healing2 = fact1.create_evolved()
    tfc1 = fact3.create_base()
    tfc2 = fact4.create_evolved()
    aqua1 = fact4.create_base()
    aqua2 = fact4.create_evolved()
    aggres = AggressiveStrategy()
    norm = NormalStrategy()
    defen = DefensiveStrategy()

    new_list: list[tuple[Creature | CreatureFactory, BattleStrategy], ...] = []
    crea_list: list[Creature] = [flame1, flame2,
                                 healing1, healing2,
                                 tfc1, tfc2,
                                 aqua1, aqua2]
    factor_list: list[CreatureFactory] = [fact1, fact2,
                                          fact3, fact4]
    strategy: list[BattleStrategy] = [aggres, norm, defen]

    for i in str_list:
        liste: list = []
        _valid = False
        my_list = i.split("+")
        for j in crea_list:
            if my_list[0] in j.name:
                liste.append(j)
                _valid = True
                break
        if not _valid:
            for k in factor_list:
                if my_list[0] in k.name:
                    liste.append(k)
                    _valid = True
                    break
        if not _valid:
            continue
        for j in strategy:
            if my_list[1] in j.name:
                liste.append(j)
                break
        new_list.append(tuple(liste))

    print("Tournament 0 (basic)")
    print(str_list)
    print("*** Tournament ***")
    print(f"{len(new_list)} opponents involved")
    print("\n* Battle *")
    first = True
    for i in new_list:
        n1, _ = i
        n = n1
        if not isinstance(n1, Creature):
            n = n1.create_base()
        if first is True:
            print(n.describe())
            print(" vs.")
            first = False
        else:
            print(n.describe())
    print("now fight!")
    for i in new_list:
        crea, stra = i
        if not isinstance(crea, Creature):
            crea = crea.create_base()
        print(stra.act(crea))


if __name__ == "__main__":
    batlle([("Flameling+Normal"), ("Healing+Defensive")])
