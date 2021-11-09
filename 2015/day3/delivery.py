def load_input():
    f = open("day3/input", "r")
    return f


def update_location(ctx, person):
    x = person[0]
    y = person[1]
    if ctx == "^":
        y += 1
    elif ctx == "v":
        y -= 1
    elif ctx == ">":
        x += 1
    elif ctx == "<":
        x -= 1

    return (x, y)


def append_location(houses, person):
    if person in houses:
        return
    else:
        houses.append(person)


def part_1(f):
    houses = [(0, 0)]
    santa_location = (0, 0)

    inputData = f.read()

    for ctx in inputData:
        santa_location = update_location(ctx, santa_location)
        append_location(houses, santa_location)

    print("Santa visited " + str(len(houses)) + " houses in one night.")


def part_2(f):
    f.seek(0)

    houses = [(0, 0)]

    santa_location = (0, 0)
    robo_location = (0, 0)
    index = 0

    inputData = f.read()

    for ctx in inputData:
        if index % 2 == 0:
            santa_location = update_location(ctx, santa_location)
            append_location(houses, santa_location)
        else:
            robo_location = update_location(ctx, robo_location)
            append_location(houses, robo_location)

        index += 1

    print("Santa and Robo-Santa visited " + str(len(houses)) +
          " houses collectively in one night.")


def delivery():
    f = load_input()

    part_1(f)
    part_2(f)


if __name__ == "__main__":
    delivery()
