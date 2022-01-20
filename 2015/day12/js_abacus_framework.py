import json

total = 0


def iterlist(l):
    sum = 0
    for v in l:
        if isinstance(v, dict):
            sum += iterdict(v)
        elif isinstance(v, list):
            sum += iterlist(v)
        elif isinstance(v, int):
            sum += v

    return sum


def iterdict(d):
    sum = 0

    for k, v in d.items():
        if isinstance(v, dict):
            sum += iterdict(v)
        elif isinstance(v, list):
            sum += iterlist(v)
        elif isinstance(v, int):
            sum += v
        elif isinstance(v, str) and v == "red":
            return 0

    return sum


def js_abacus():
    f = open('input.json')

    data = json.load(f)

    global total

    if isinstance(data, dict):
        total = iterdict(data)
    elif isinstance(data, list):
        total = iterlist(data)

    print(total)


if __name__ == "__main__":
    js_abacus()
