from audioop import reverse
from itertools import permutations


def load_input(file):
    f = open(file, "r")
    return f.readlines()


def make_list(file):
    list = []
    for number in load_input(file):
        list.append(int(number.strip()))
    return list


def process_input(list):
    max_volume = 150
    tracking_index = 1
    lst = 1
    current_index = 0
    result = 0

    list.sort(reverse=True)

    stack = [(0, list[0])]

    volume = list[0]

    print(list)

    while True:
        volume += list[tracking_index]
        stack.append((tracking_index, list[tracking_index]))

        if volume > max_volume:
            volume -= stack[-1][0]
            stack.pop()

        if volume == max_volume:
            print("match", tracking_index, volume, stack)
            result += 1
            volume -= stack[-1]
            stack.pop()
            tracking_index += 1
        else:
            tracking_index += 1

        if tracking_index == len(list):
            idx, val = stack.pop()

            if len(stack) == 0:
                idx += 1
                stack.append((idx, list[idx]))
                print("done?")
                break

            volume -= val
            tracking_index = idx + 1

            # lst += 1
            # if lst == len(list):
            #     current_index += 1
            #     stack = [list[current_index]]
            #     volume = list[current_index]
            #     tracking_index = current_index + 1
            #     lst = tracking_index
            #     print("ci", current_index)
            # else:
            #     tracking_index = lst
            #     volume = list[current_index]
            #     stack = [list[current_index]]

            if current_index == len(list) - 1:
                print("DONE PLEASE")
                break

    print(result)


if __name__ == "__main__":
    list = make_list("input")
    process_input(list)
