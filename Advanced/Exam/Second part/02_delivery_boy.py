ROWS, COLUMNS = (int(x) for x in input().split())
direction_mapper = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}


def get_info():
    start_position = []
    matrix = []
    for row in range(ROWS):
        line = list(input())
        matrix.append(line)
        if "B" in line:
            start_position = [row, line.index("B")]
    return matrix, start_position


field, position = get_info()
start = position.copy()
while True:
    command = input()
    row, col = [x + y for x, y in zip(direction_mapper[command], position)]
    if row in range(ROWS) and col in range(COLUMNS):

        if field[row][col] == "P":
            field[row][col] = "R"
            print("Pizza is collected. 10 minutes for delivery.")

        elif field[row][col] == "A":
            field[row][col] = "P"
            print("Pizza is delivered on time! Next order...")
            field[start[0]][start[1]] = "B"
            break
        elif field[row][col] == "*":
            continue

        if field[row][col] != "R" and field[row][col] != "P":
            field[row][col] = "."
        position = [row, col]

    else:
        field[start[0]][start[1]] = " "
        print("The delivery is late. Order is canceled.")
        break

[print(*el, sep="") for el in field]
