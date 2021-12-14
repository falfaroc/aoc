def open_input():
    input = open("input", "r")
    inputData = input.readlines()
    input.close
    clean = []
    for line in inputData:
        clean.append(line.strip())
    return clean


def decode_esape(line, start):
    if line[start + 1] == "\\" or line[start + 1] == '"':
        escape_len = 1
    elif line[start + 1] == "x":
        escape_len = 3
    return escape_len


def enlarge_esape(line, start):
    skip = 0
    if line[start + 1] == "\\":
        escape_len = 4
        skip = 1
    elif line[start + 1] == '"':
        escape_len = 4
        skip = 1
    elif line[start + 1] == "x":
        escape_len = 2
    return skip, escape_len


def shrinky_dink(dat):
    memory_chars = []
    for line in dat:
        current_count = 0
        skip = 0
        for i in range(0, len(line)):
            if skip > 0:
                skip -= 1
                continue
            if line[i] == '"':
                continue
            elif line[i] == "\\":
                e_l = decode_esape(line, i)
                skip += e_l
                current_count += 1
            else:
                current_count += 1
        memory_chars.append(current_count)
    return sum(memory_chars)


def biggening_ray(dat):
    memory_chars = []
    for line in dat:
        current_count = 0
        skip = 0
        for i in range(0, len(line)):
            if skip > 0:
                skip -= 1
                continue
            if line[i] == '"':
                current_count += 3
            elif line[i] == "\\":
                skip, escape_val = enlarge_esape(line, i)
                current_count += escape_val
            else:
                current_count += 1
        memory_chars.append(current_count)
    return sum(memory_chars)


def get_total(data):
    total_chars = []
    for line in data:
        total_chars.append(len(line))
    return sum(total_chars)


def matchsticks():
    dat = []
    dat = open_input()

    a = get_total(dat)
    b = shrinky_dink(dat)
    c = biggening_ray(dat)

    print("Part 1 Ans:", a - b, "Part 2:", c - a)


if __name__ == "__main__":
    matchsticks()
