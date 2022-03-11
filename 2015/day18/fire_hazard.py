import numpy as np

depth = 100
levels = 1


def load_input():
    f = open("input", "r")
    return f.readlines()


def neighbors(matrix, rowNumber, colNumber):
    result = 0
    for rowAdd in range(-1, 2):
        newRow = rowNumber + rowAdd
        if newRow >= 0 and newRow <= len(matrix)-1:
            for colAdd in range(-1, 2):
                newCol = colNumber + colAdd
                if newCol >= 0 and newCol <= len(matrix)-1:
                    if newCol == colNumber and newRow == rowNumber:
                        continue
                    if matrix[newRow][newCol] == 1:
                        result += 1
    return result


def check_neighbours(i, j, grid):
    count = neighbors(grid, i, j)
    if grid[i][j] == 1:
        return count == 2 or count == 3
    else:
        return count == 3


def is_corner(i, j, grid):
    shape = grid.shape
    if i == 0 and j == 0:
        return True
    if i == 0 and j == shape[0] - 1:
        return True
    if i == shape[1]-1 and j == 0:
        return True
    if i == shape[1]-1 and j == shape[0] - 1:
        return True
    return False


def process(grid):
    shape = grid.shape
    grid[0][0] = 1
    grid[0][shape[0] - 1] = 1
    grid[shape[1]-1][0] = 1
    grid[shape[1]-1][shape[0] - 1] = 1

    for steps in range(0, 100):
        old_grid = grid.copy()
        for i in range(depth):
            for j in range(depth):
                if is_corner(i, j, grid):
                    continue
                if check_neighbours(i, j, old_grid):
                    grid[i][j] = 1
                else:
                    grid[i][j] = 0
        # print("STEP:", steps)
        # print(grid)


def parse_grid(lines):
    x = 0
    y = 0

    grid = np.zeros((depth, depth))

    for line_x in lines:
        for element_y in line_x:
            if element_y == "\n":
                continue

            if(element_y == "."):
                grid[x][y] = 0
            elif(element_y == "#"):
                grid[x][y] = 1
            y += 1
        x += 1
        y = 0

    return grid


def fire_hazard():
    lines = load_input()
    grid = parse_grid(lines)

    print(grid)

    process(grid)

    count = 0

    for i in range(depth):
        for j in range(depth):
            if grid[i][j] == 1:
                count += 1
    print("LIGHTS THAT ARE ON:", count)


if __name__ == "__main__":
    fire_hazard()
