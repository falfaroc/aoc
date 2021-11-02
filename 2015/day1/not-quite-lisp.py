def load_file():
    f = open("input", "r")
    return f


def what_floor(f):
    input = f.readline()
    result = input.count("(") - input.count(")")

    print("Deliver the presents to floor " + str(result))


def basement_index(f):
    f.seek(0)
    result = 0

    input = f.readline()
    for element in range(0, len(input)):
        if input[element] == '(':
            result = result + 1
        else:
            result = result - 1

        if result == -1:
            return element + 1


def santa():
    f = load_file()
    what_floor(f)

    print("Index that took Santa to the basement: " + str(basement_index(f)))
    f.close()


if __name__ == "__main__":
    santa()
