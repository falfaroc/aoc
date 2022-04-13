class Charecter:
    armor = 0
    attack = 0
    life = 0

    def __init__(self, armor, attack, life):
        self.armor = armor
        self.attack = attack
        self.life = life

    def change_attack_value(self, attack):
        self.attack = attack

    def change_armor_value(self, armor):
        self.attack = armor

    def take_damage(self, damage):
        self.life -= max(1, damage - self.armor)
        return self.life


def load_input(file):
    f = open(file, "r")
    return f.readlines()


def parse(file):
    for each in load_input(file):
        things = each.split(" ")
        if things[0] == "Hit":
            hp = int(things[2].strip())
        elif things[0] == "Damage:":
            dmg = int(things[1].strip())
        elif things[0] == "Armor:":
            arm = int(things[1].strip())
    return Charecter(arm, dmg, hp)


def Shop(characters):
    player_hp = 100
    weapons = [(8, 4), (10, 5), (25, 6), (40, 7), (74, 8)]
    armor = [(0, 0), (13, 1), (31, 2), (53, 3), (75, 4), (102, 5)]
    rings = [(25, 1, 0), (50, 2, 0), (100, 3, 0),
             (20, 0, 1), (40, 0, 2), (80, 0, 3)]
    min_cost = 356
    max_cost = 0
    for stabber in weapons:
        for arm in armor:
            for i in range(0, 7):
                if i != 0:
                    ring_1 = rings[i-1]
                else:
                    ring_1 = (0, 0, 0)
                for j in range(0, 7):
                    if j != 0 and j != i:
                        ring_2 = rings[j-1]
                    else:
                        ring_2 = (0, 0, 0)
                    cost = stabber[0] + arm[0] + ring_1[0] + ring_2[0]
                    characters["Player"] = Charecter(
                        arm[1] + ring_1[2] + ring_2[2], stabber[1] + ring_1[1] + ring_2[1], player_hp)
                    if fight(characters):
                        if cost < min_cost:
                            min_cost = cost
                    else:
                        if cost > max_cost:
                            max_cost = cost
                    del characters["Player"]
    return min_cost, max_cost

# Returns true if the player wins the fight


def fight(characters):
    characters["Boss"] = parse("input")
    while characters["Boss"].take_damage(characters["Player"].attack) > 0:
        if characters["Player"].take_damage(characters["Boss"].attack) <= 0:
            return False
    return True


def rpg_simulator():
    characters = {}
    least_cost, most_cost = Shop(characters)
    print("Lowest Winning Cost: ", least_cost,
          "\nHighest Losing Cost: ", most_cost)


if __name__ == "__main__":
    rpg_simulator()
