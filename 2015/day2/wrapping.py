def load_input():
    f = open("input", "r")
    return f


def calculate_square_feet(l, w, h):
    return 2*l*w + 2*w*h + 2*h*l


def calculate_min_area(l, w, h):
    return min(l*w, w*h, h*l)


def calculate_ribbon_length(l, w, h):
    area = l*w*h
    min_perim = min(l+w, w+h, h+l) * 2

    return area + min_perim


def calculate_ribbon_required(file):
    file.seek(0)

    result = 0

    lines = file.readlines()

    for line in lines:
        ctx = line.split("x")
        l = int(ctx[0])
        w = int(ctx[1])
        h = int(ctx[2])

        result = result + calculate_ribbon_length(l, w, h)

    print("The elves' need to order " + str(result) + " feet of ribbon")


def calculate_paper_needed(file):
    result = 0

    lines = file.readlines()

    for line in lines:
        ctx = line.split("x")
        l = int(ctx[0])
        w = int(ctx[1])
        h = int(ctx[2])

        result = result + calculate_square_feet(l, w, h)
        result = result + calculate_min_area(l, w, h)

    print("The elves' need to order " + str(result) + " square feet")


def wrapping():
    f = load_input()

    calculate_paper_needed(f)
    calculate_ribbon_required(f)


if __name__ == "__main__":
    wrapping()
