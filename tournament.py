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


def batlle(str_list: list) -> None:
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

    new_list: list[tuple[Creature | CreatureFactory, BattleStrategy]] = []
    crea_list: list[Creature] = [flame1, flame2,
                                 healing1, healing2,
                                 tfc1, tfc2,
                                 aqua1, aqua2]
    factor_list: list[CreatureFactory] = [fact1, fact2,
                                          fact3, fact4]
    strategy: list[BattleStrategy] = [aggres, norm, defen]

    print(str_list)
    str_list = [i.strip("()") for i in str_list]
    for i in str_list:
        factor: Creature | CreatureFactory | None = None
        strat: BattleStrategy | None = None
        my_list = i.split("+")
        for j in crea_list:
            if my_list[0] in j.name:
                factor = j
                break
        if not factor:
            for k in factor_list:
                if my_list[0] in k.name:
                    factor = k
                    break
        if not factor:
            continue
        for p in strategy:
            if my_list[1] in p.name:
                strat = p
                break
        if factor and strat:
            new_list.append((factor, strat))

    print("*** Tournament ***")
    print(f"{len(new_list)} opponents involved")
    list_of_two: list[tuple[Creature | CreatureFactory, BattleStrategy]] = []
    ku = 0
    fro = True
    while ku < len(new_list) - 1:
        bk = ku + 1
        while bk < len(new_list):
            print("\n* Battle *")
            first = True
            list_of_two = [new_list[ku], new_list[bk]]
            for a in list_of_two:
                n1, _ = a
                n = n1
                if isinstance(n1, CreatureFactory):
                    n = n1.create_base()
                else:
                    n = n1
                if first is True:
                    print(n.describe())
                    print(" vs.")
                    first = False
                else:
                    print(n.describe())
            print(" now fight!")
            for z in list_of_two:
                crea, stra = z
                if not isinstance(crea, Creature):
                    crea = crea.create_base()
                if stra.is_valid(crea):
                    print(stra.act(crea))
                else:
                    print(stra.act(crea))
                    fro = False
                    break
            if not fro:
                break
            bk += 1
        if not fro:
            break
        ku += 1


if __name__ == "__main__":
    print("Tournament 0 (basic)")
    batlle([("(Flameling+Normal)"), ("(Healing+Defensive)")])
    print("\nTournament 1 (error)")
    batlle([("(Flameling+Aggressive)"), ("(Healing+Defensive)")])
    print("\nTournament 2 (multiple)")
    batlle([("(Aquabub+Normal)"),
            ("(Healing+Defensive)"),
            ("(Transform+Aggressive)")])
