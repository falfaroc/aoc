keywords = ["toggle ", "turn off ", "turn on "]

lights = [[0 for i in range(1000)] for j in range(1000)]
brigthness = [[0 for i in range(1000)] for j in range(1000)]


def load_input():
    f = open("input", "r")
    return f


def split_content(line):
    sides = line.split(" through ")
    lhs = sides[0].split(",")
    rhs = sides[1].split(",")

    return int(lhs[0]), int(lhs[1]), int(rhs[0]), int(rhs[1])


def calculate_lights_change(x1, y1, x2, y2, command):
    x = x1
    y = y1

    while x <= x2:
        while y <= y2:
            if command in keywords[0]:
                toggle(x, y)
            elif command in keywords[1]:
                turn_off(x, y)
            else:
                turn_on(x, y)

            y += 1

        y = y1
        x += 1


def toggle(x, y):
    if lights[x][y] == 0:
        lights[x][y] = 1
    else:
        lights[x][y] = 0

    brigthness[x][y] += 2


def turn_off(x, y):
    lights[x][y] = 0

    if(brigthness[x][y] > 0):
        brigthness[x][y] -= 1


def turn_on(x, y):
    lights[x][y] = 1

    brigthness[x][y] += 1


def parse_command(line):
    ctx = ""
    command = ""

    if keywords[0] in line:
        command = keywords[0]
        ctx = line.split(keywords[0])[1]
    elif keywords[1] in line:
        command = keywords[1]
        ctx = line.split(keywords[1])[1]
    elif keywords[2] in line:
        command = keywords[2]
        ctx = line.split(keywords[2])[1]

    x1, y1, x2, y2 = split_content(ctx)

    calculate_lights_change(x1, y1, x2, y2, command)


def calculate_fire_hazard(file):

    lines = file.readlines()

    for line in lines:
        parse_command(line)


def fire_hazard():
    f = load_input()

    calculate_fire_hazard(f)

    lights_on_count = 0
    brigthness_level = 0

    for x in range(len(lights[0])):
        for y in range(len(lights[1])):
            if lights[x][y] == 1:
                lights_on_count += 1

            brigthness_level += brigthness[x][y]

    print("The number of lights lit by the elves are", lights_on_count)
    print("Total brightness after Santa's instructions is", brigthness_level)


if __name__ == "__main__":
    fire_hazard()
