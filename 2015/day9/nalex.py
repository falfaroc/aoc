def open_input():
    input = open("input", "r")
    inputData = input.readlines()
    input.close
    clean = []
    for line in inputData:
        clean.append(line.strip())
    return clean


class trip:
    path = []
    cost = 0

    def __init__(self, in_path, dest, in_cost, dest_cost):
        self.path = in_path[:]
        self.path.append(dest)
        self.cost = int(in_cost) + int(dest_cost)


places = []
for line in open_input():
    s = line.split(" to ")
    d1 = s[0]
    s = s[1].split(" = ")
    places.append(((d1, s[0]), s[1]))
print(places)
starts = []
paths = []
for each in places:
    if each[0][0] not in starts:
        starts.append(each[0][0])
        paths.append(trip([], each[0][0], 0, 0))
    elif each[0][1] not in starts:
        starts.append(each[0][1])
        paths.append(trip([], each[0][1], 0, 0))
done = []
while len(paths) > 0:
    s = paths.pop(0)
    # print(s.path)
    for each in places:
        if each[0][0] not in s.path and each[0][1] == s.path[-1]:
            paths.append(trip(s.path, each[0][0], s.cost, each[1]))
        elif each[0][1] not in s.path and each[0][0] == s.path[-1]:
            paths.append(trip(s.path, each[0][1], s.cost, each[1]))
    if len(s.path) == len(starts):
        done.append(s)
min = 9999
max = 0

print(done)
for each in done:
    if each.cost < min:
        min = each.cost
    elif each.cost > max:
        max = each.cost
print("the lowest cost is", min, "higest", max)
