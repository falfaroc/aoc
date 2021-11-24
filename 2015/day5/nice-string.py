def load_input():
    f = open("input", "r")
    return f


def in_a_row(ctx):
    prev = ""

    for x in ctx:
        if x == prev:
            return True
        prev = x

    return False


def is_double_double(ctx):
    for x in range(0, len(ctx) - 2):
        if ctx[x] + ctx[x+1] in ctx[x+2:]:
            return True

    return False


def is_triple(ctx):
    for x in range(0, len(ctx) - 2):
        if ctx[x] == ctx[x + 2]:
            return True

    return False


def contains_three_vowels(ctx):
    result = ctx.count("a") + ctx.count("e")+ctx.count("i") + \
        ctx.count("o")+ctx.count("u")

    return result


def is_valid(ctx):
    if "ab" in ctx or "cd" in ctx or "pq" in ctx or "xy" in ctx:
        return False

    return True


def calculate_nice_strings(file):
    nice_count = 0

    lines = file.readlines()

    for line in lines:
        if not is_valid(str(line)):
            continue

        if contains_three_vowels(str(line)) < 3:
            continue

        if not in_a_row(line):
            continue

        nice_count += 1

    print("The elves found " + str(nice_count) + " nice strings")


def calculate_nice_strings_pt_2(file):
    file.seek(0)
    nice_count = 0

    lines = file.readlines()

    for line in lines:
        if not is_double_double(line):
            continue

        if not is_triple(line):
            continue

        nice_count += 1

    print("The elves found " + str(nice_count) + " nice strings pt 2")


def nice_string():
    f = load_input()

    calculate_nice_strings(f)

    calculate_nice_strings_pt_2(f)


if __name__ == "__main__":
    nice_string()
