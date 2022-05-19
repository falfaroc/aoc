class spell:
    def __init__(self, name, cost, damage=0, length=0, heal=0, armor=0, recharge=0):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.length = length
        self.heal = heal
        self.armor = armor
        self.recharge = recharge

    def __str__(self):
        return "Name: " + self.name + " Cost: " + str(self.cost) + " Damage: " + str(self.damage) + " Length: " + str(self.length)


class charater:
    def __init__(self, hp, damage=0, mp=0):
        self.hp = hp
        self.damage = damage
        self.mp = mp

    def __str__(self):
        return "HP: " + str(self.hp) + " Damage: " + str(self.damage) + " MP: " + str(self.mp)


def load_input(file):
    f = open(file, "r")
    return f.readlines()


def load_boss():
    for each in load_input("input"):
        things = each.split(" ")
        if things[0] == "Hit":
            hp = int(things[2].strip())
        elif things[0] == "Damage:":
            damage = int(things[1].strip())
    return charater(hp, damage=damage)


def load_spells():
    spells = []

    spells.append(spell(name="Magic Missile", cost=53, damage=4))
    spells.append(spell(name="Drain", cost=73, damage=2, heal=2))
    spells.append(spell(name="Shield", cost=113, length=6, armor=7))
    spells.append(spell(name="Poison", cost=173, damage=3, length=6))
    spells.append(spell(name="Recharge", cost=229, length=5, recharge=101))

    return spells


def wizard_simulator():
    player = charater(50, mp=500)
    spells = load_spells()
    boss = load_boss()
    print("Player:", player)

    for ctx in spells:
        print(ctx)

    print("Boss:", boss)


if __name__ == "__main__":
    wizard_simulator()
