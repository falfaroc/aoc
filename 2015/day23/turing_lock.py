def load_input(file):
    f = open(file, "r")
    lines = []
    for each in f.readlines():
        instructions = each.split(",")
        if len(instructions) == 1:
            inst_reg = instructions[0].split(" ")
            if inst_reg[0] == "jmp":
                lines.append(
                    (inst_reg[0].strip(), int(inst_reg[1].strip()), 0))
            else:
                lines.append((inst_reg[0].strip(), inst_reg[1].strip(), 0))
        else:
            inst_reg = instructions[0].split(" ")
            lines.append(
                (inst_reg[0].strip(), inst_reg[1].strip(),
                 int(instructions[1].strip()))
            )
    return lines


def compute(process, reg_a, reg_b):
    inst_index = 0
    while inst_index < len(process):
        current_process = process[inst_index]
        # hlf r sets register r to half its current value, then continues with the next instruction.
        if current_process[0] == "hlf":
            if current_process[1] == "a":
                reg_a /= 2
            else:
                reg_b /= 2
            inst_index += 1

        # tpl r sets register r to triple its current value, then continues with the next instruction.
        elif current_process[0] == "tpl":
            if current_process[1] == "a":
                reg_a *= 3
            else:
                reg_b *= 3
            inst_index += 1

        # inc r increments register r, adding 1 to it, then continues with the next instruction.
        elif current_process[0] == "inc":
            if current_process[1] == "a":
                reg_a += 1
            else:
                reg_b += 1
            inst_index += 1

        # jmp offset is a jump; it continues with the instruction offset away relative to itself
        elif current_process[0] == "jmp":
            inst_index += current_process[1]

        # jie r, offset is like jmp, but only jumps if register r is even ("jump if even")
        elif current_process[0] == "jie":
            if current_process[1] == "a":
                if reg_a % 2 == 0:
                    inst_index += current_process[2]
                else:
                    inst_index += 1
            else:
                if reg_b % 2 == 0:
                    inst_index += current_process[2]
                else:
                    inst_index += 1

        # jio r, offset is like jmp, but only jumps if register r is 1 ("jump if one", not odd)
        elif current_process[0] == "jio":
            if current_process[1] == "a":
                if reg_a == 1:
                    inst_index += current_process[2]
                else:
                    inst_index += 1
            else:
                if reg_b == 1:
                    inst_index += current_process[2]
                else:
                    inst_index += 1

    return reg_b


def turing_lock():
    process = load_input("input")
    print("part 1: ", compute(process, 0, 0))
    print("part 2: ", compute(process, 1, 0))


if __name__ == "__main__":
    turing_lock()
