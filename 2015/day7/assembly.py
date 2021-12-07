
import numpy as np


def and_op(x, y):
    return x & y


def or_op(x, y):
    return x | y


def lshift_op(x, shift):
    return x << shift


def rshift_op(x, shift):
    return x >> shift


def not_op(x):
    return np.uint16(~x)


operations = {"AND": and_op,
              "OR": or_op,
              "LSHIFT": lshift_op,
              "RSHIFT": rshift_op,
              "NOT": not_op,
              }

elements = []


def load_input():
    f = open("input", "r")
    return f


def is_valid(instruction, registers):
    elements.clear()

    if instruction[0].isnumeric() and instruction[2] in registers:
        elements.append(instruction[0])
        elements.append(registers.get(instruction[2]))
    elif instruction[2].isnumeric() and instruction[0] in registers:
        elements.append(registers.get(instruction[0]))
        elements.append(instruction[2])
    elif instruction[0] in registers and instruction[2] in registers:
        elements.append(registers.get(instruction[0]))
        elements.append(registers.get(instruction[2]))

    return len(elements) > 0


def calculate_instructions(registers, instructions):
    # Iterate through the instructions.
    while len(instructions) > 0:
        instruction = instructions.pop(0)

        ctx = instruction[1].split()

        if len(ctx) == 1 and ctx[0] in registers:
            result = registers[ctx[0]]
            registers[instruction[0]] = int(result)

        elif len(ctx) == 2 and "NOT" in ctx[0] and ctx[1] in registers:
            x = registers[ctx[1]]
            result = operations[ctx[0]](x)
            registers[instruction[0]] = int(result)

        elif len(ctx) == 3 and is_valid(ctx, registers):
            x = elements[0]
            y = elements[1]

            result = operations[ctx[1]](int(x), int(y))

            registers[instruction[0]] = int(result)

        else:
            instructions.append(instruction)

    return registers


def assembly():
    f = load_input()

    registers = {}
    instructions = []

    lines = f.readlines()

    # Separate between register and instructions.
    for instruction in lines:
        inst = instruction.split(" -> ")

        if inst[0].isnumeric():
            registers[inst[1].strip()] = int(inst[0])
        else:
            instructions.append((inst[1].strip(), inst[0].strip()))

    register_dos = registers.copy()
    instructions_dos = instructions.copy()

    calculate_instructions(registers, instructions)

    print("Part 1: Value of wire (a):", registers['a'])

    register_dos['b'] = registers['a']

    calculate_instructions(register_dos, instructions_dos)

    print("Part 2: Value of wire (a):", register_dos['a'])


if __name__ == "__main__":
    assembly()
