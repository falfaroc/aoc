import re


molecule_re = re.compile(r"[A-Z][a-z]*")


def load_input(file):
    f = open(file, "r")
    return f.readlines()


def parse(file):
    swaps = {}
    start_molecule = []
    for each in load_input(file):
        if "=>" in each:
            # print(each)
            line = each.split("=>")
            line[0] = line[0].strip()
            if line[0] in swaps.keys():
                swaps[line[0]].append(line[1].strip())
            else:
                swaps[line[0]] = [line[1].strip()]
        elif each != "\n":
            start_molecule = molecule_re.findall(each.strip())

    return start_molecule, swaps


def make_swap(start, idx, swaps, Moleculies):
    temp = start.copy()
    for thing in swaps[start[idx]]:
        temp[idx] = thing
        temp2 = "".join(temp)
        if temp2 not in Moleculies:
            Moleculies.append(temp2)
        temp = start.copy()
    return Moleculies


def medicine():
    start, swaps = parse("input")

    Moleculies = []

    for i in range(0, len(start)):
        if start[i] in swaps.keys():
            Moleculies = make_swap(start, i, swaps,  Moleculies)

    print(len(Moleculies))


if __name__ == "__main__":
    medicine()
