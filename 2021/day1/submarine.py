window_size = 3


def load_file():
    f = open("input", "r")
    return f


def number_of_increases(file):
    result = 0

    lines = file.readlines()
    prev = int(lines[0])
    current = 0

    for line in lines:
        current = int(line)

        if (current > prev):
            result += 1

        prev = current

    print("The number of measurements that are greater than the previous one are:", result)


def update_window(list, element):
    if len(list) == window_size:
        list.pop(0)
        list.append(element)
    else:
        list.append(element)


def is_greater(prev, cur):
    if len(prev) == window_size and len(cur) == window_size:
        prev_sum = sum(prev)
        cur_sum = sum(cur)

        if cur_sum > prev_sum:
            return 1

    return 0


def sliding_window_increses(file):
    file.seek(0)
    result = 0

    lines = file.readlines()
    prev = []
    cur = []

    for line in lines:
        update_window(cur, int(line))
        result += is_greater(prev, cur)
        update_window(prev, int(line))

    print("The number of sums greater than the previous are:", result)


def submarine():
    f = load_file()
    number_of_increases(f)
    sliding_window_increses(f)


if __name__ == "__main__":
    submarine()
