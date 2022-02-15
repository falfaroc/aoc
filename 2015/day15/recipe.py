import numpy as np


class Ingredient:
    def __init__(self, capacity=0, durability=0, flavour=0, texture=0, calories=0):
        self.capacity = capacity
        self.durability = durability
        self.flavour = flavour
        self.calories = calories
        self.texture = texture
        self.tsp = 0

    def get_score(self):
        return self.tsp*self.capacity, self.tsp*self.durability, self.tsp*self.flavour, self.tsp*self.texture

    def get_cal(self):
        return self.tsp*self.calories


def load_input(file):
    f = open(file, "r")
    return f.readlines()


def make_list(file):
    list = []
    for each in load_input(file):
        each = each.replace(",", "")
        each = each.strip()
        split = each.split(" ")
        list.append(Ingredient(int(split[2]), int(split[4]), int(
            split[6]), int(split[8]), int(split[10])))
    return list


def get_score(tsp, list):
    score_l = []
    for i in range(0, len(list)):
        list[i].tsp = tsp[i]
    for each in list:
        score_l.append(np.array(each.get_cal()))
    score = np.zeros(score_l[0].shape)
    for each in score_l:
        score += each
    if score != 500:
        return 0
    score = 0
    score_l = []
    for i in range(0, len(list)):
        list[i].tsp = tsp[i]
    for each in list:
        score_l.append(np.array(each.get_score()))
    score = np.zeros(score_l[0].shape)
    for each in score_l:
        score += each
    final_score = 1
    for each in score:
        if each < 0:
            final_score = 0
            break
        final_score *= each
    return final_score


tsp = [0, 0, 0, 0]
list = make_list("input")
max = 0
miss = 0
hit = 0
for i in range(1, 98):
    for j in range(1, 98):
        for k in range(1, 98):
            for l in range(1, 98):
                tsp[0] = i
                tsp[1] = j
                tsp[2] = k
                tsp[3] = l
                if tsp[0] + tsp[1] + tsp[2] + tsp[3] == 100:
                    hit += 1
                    final_score = get_score(tsp, list)
                    if final_score > max:
                        max = final_score
                else:
                    miss += 1
print(max, "hit", hit, "miss", miss, "acc", hit/((hit+miss))*100)
