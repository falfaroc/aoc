import re

doubles_pattern = re.compile(r"([a-z])\1.*([a-z])\2")
invalid_pattern = re.compile(r"[ilo]")


def has_straight(input):
    for i in range(len(input) - 2):
        if ord(input[i]) == ord(input[i + 1]) - 1 and ord(input[i]) == ord(input[i + 2]) - 2:
            return True
    return False


def is_valid(input):
    if len(input) != 8:
        return False

    if not doubles_pattern.search(input):
        return False

    if invalid_pattern.search(input):
        return False

    if not has_straight(input):
        return False

    return True


def asciitize(input):
    return [ord(charecter) for charecter in input]


def increase(input):
    input[-1] += 1
    if input[-1] > 122:
        input[-1] = 97
        input[-2] += 1
        if input[-2] > 122:
            input[-2] = 97
            input[-3] += 1
            if input[-3] > 122:
                input[-3] = 97
                input[-4] += 1
                if input[-4] > 122:
                    input[-4] = 97
                    input[-5] += 1
                    if input[-5] > 122:
                        input[-5] = 97
                        input[-6] += 1
                        if input[-7] > 122:
                            input[-7] = 97
                            input[-8] += 1

    return [chr(charecter) for charecter in input]


def corporate_policy():
    input = "hepxxyzz"

    input = asciitize(input)
    input = increase(input)
    input = ''.join(input)

    while not is_valid(input):
        input = asciitize(input)
        input = increase(input)
        input = ''.join(input)

    print(input)


if __name__ == "__main__":
    corporate_policy()
