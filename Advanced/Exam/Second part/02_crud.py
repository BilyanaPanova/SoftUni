SIZE = 6


def directions(row, col, d):
    direction_mapper = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}
    next_r, next_c = direction_mapper[d][0] + row, direction_mapper[d][1] + col
    if next_r in range(SIZE) and next_c in range(SIZE):
        return next_r, next_c


def create(field, row, col):
    val = value
    if field[row][col] == ".":
        field[row][col] = val
    return field


def update(field, row, col):
    val = value
    if field[row][col] != ".":
        field[row][col] = val
    return field


def delete(field, row, col):
    if field[row][col] != ".":
        field[row][col] = "."
    return field


def read(field, row, col):
    if field[row][col] != ".":
        print(field[row][col])
    return field


matrix = [input().split() for _ in range(SIZE)]
start_r, start_c = [int(x) for x in input().strip("()").split(", ")]

while True:
    commands = input()
    if commands == "Stop":
        [print(*el) for el in matrix]
        break

    try:
        command, direction, value = commands.split(", ")
    except ValueError:
        command, direction = commands.split(", ")

    mapper = {"Create": create, "Update": update, "Delete": delete, "Read": read}
    r, c = directions(start_r, start_c, direction)
    matrix = mapper[command](matrix, r, c)
    start_r, start_c = r, c
