class Reindeer:
    def __init__(self, name="", speed=0, run=0, rest=0):
        self.name = name
        self.speed = speed
        self.run = run
        self.rest = rest
        self.state = "running"
        self.time_in_state = 0
        self.length = 0
        self.score = 0

    def swap_state(self):
        if self.state == "running":
            self.state = "resting"
            self.time_in_state = 1
        else:
            self.state = "running"
            self.time_in_state = 0

    def increase_score(self):
        self.score += 1

    def tick_time(self):
        self.time_in_state += 1
        if self.state == "running":
            if self.time_in_state > self.run:
                self.swap_state()
                return
            self.length += self.speed
        else:
            if self.time_in_state >= self.rest:
                self.swap_state()
                return


def load_input(file):
    f = open(file, "r")
    return f.readlines()


def make_list(file):
    list = []
    for each in load_input(file):
        split = each.split(" ")
        list.append(Reindeer(split[0], int(split[3]),
                    int(split[6]), int(split[13])))
    return list


def calulate_winner(list, time):
    for second in range(1, time+1):
        leader = Reindeer()
        for each in list:
            each.tick_time()
            # print("\n", second, "Reindeer:", each.name, "\nDistance:", each.length, each.state, each.time_in_state)
            if each.length > leader.length:
                leader = each
        for each in list:
            if each.length == leader.length and each.name is not leader.name:
                each.increase_score()
        leader.increase_score()
    max = 0
    for each in list:
        if each.score > max:
            max = each.score
    max_dist = 0
    for each in list:
        if each.length > max_dist:
            max_dist = each.length
    return max, max_dist


if __name__ == "__main__":
    list = make_list("input")
    print(calulate_winner(list, 2503))
