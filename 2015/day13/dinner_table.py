from itertools import permutations


class Guest:
    def __init__(self, name):
        self.name = name
        self.happiness = {}

    def add_happiness_case(self, guest, score):
        self.happiness[guest] = score


def load_input():
    f = open("input", "r")
    return f.readlines()


def calc_score(mod, mag):
    if mod == "lose":
        return -int(mag)
    return int(mag)


def determine_happiness(guest_list, seating):
    score = 0

    score += guest_list[seating[0]].happiness[seating[-1]]
    score += guest_list[seating[-1]].happiness[seating[0]]

    for i in range(1, len(seating)):
        score += guest_list[seating[i-1]].happiness[seating[i]]
        score += guest_list[seating[i]].happiness[seating[i-1]]

    return score


def calculate_seating_order(guest_list):
    guests = sorted(guest_list.keys())

    happiness_seatings = []
    for seating in permutations(guests[1:]):
        seating_order = [guests[0]]+list(seating)
        score = determine_happiness(guest_list, seating_order)

        happiness_seatings.append([(score, seating_order)])

    happiness_seatings.sort()

    return happiness_seatings[-1]


def process_input(file):
    guest_list = {}
    split_list = []

    for each in file:
        each = each.strip("\n")
        each = each.strip(".")
        split_list = each.split(" ")

        if split_list[0] not in guest_list:
            guest_list[split_list[0]] = Guest(split_list[0])

        guest_list[split_list[0]].add_happiness_case(
            split_list[10], calc_score(split_list[2], split_list[3]))

    print("Part One.")
    result = calculate_seating_order(guest_list)
    print("Seating Order:", result[0][1])
    print("Happiness Score:", result[0][0])

    print("\nPart Dos.")
    guest_list["me"] = Guest("me")

    for key in guest_list:
        guest_list[key].add_happiness_case("me", 0)
        guest_list["me"].add_happiness_case(key, 0)

    result = calculate_seating_order(guest_list)
    print("Seating Order:", result[0][1])
    print("Happiness Score:", result[0][0])


if __name__ == "__main__":
    process_input(load_input())
