from functools import reduce


def factor_sum(n):
    return sum(set(reduce(list.__add__,
                          ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))


def factors(n):
    return set(reduce(list.__add__,
                      ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


def part_1(goal):
    i = 1
    while True:
        if factor_sum(i)*10 >= goal:
            print("The first house is: ", i)
            break
        i += 1


def part_2(goal):
    i = 1
    while True:
        fact = factors(i)
        fact_copy = fact.copy()
        for each in fact:
            if i/each > 50:
                fact_copy.remove(each)
        if sum(fact_copy)*11 >= goal:
            print("The first house with lazy eleves is: ", i)
            break
        i += 1


def infinite_elves():
    goal = 29000000

    part_1(goal)
    part_2(goal)


if __name__ == "__main__":
    infinite_elves()
