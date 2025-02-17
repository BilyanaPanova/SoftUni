def get_info():
    start_position = []
    matrix = []
    for row in range(size):
        line = list(input())
        if "P" in line:
            start_position.extend([row, line.index("P")])
            line[line.index("P")] = "-"
        matrix.append(line)
    return start_position, matrix


size = int(input())
health = 100
direction_mapper = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}
position, field = get_info()
while True:
    move = input()
    curr_row, curr_col = [x + y for x, y in zip(position, direction_mapper[move])]
    if curr_row in range(size) and curr_col in range(size):
        position = [curr_row, curr_col]
        mark = field[curr_row][curr_col]
        if mark == "M":
            health -= 40
            if health > 0:
                field[curr_row][curr_col] = "-"
            else:
                health = 0
                print("Player is dead. Maze over!")
                break
        elif mark == "X":
            print("Player escaped the maze. Danger passed!")
            break
        elif mark == "H":
            health = min(health + 15, 100)
            field[curr_row][curr_col] = "-"

print(f"Player's health: {health} units")
field[position[0]][position[1]] = "P"
[print(*el, sep="") for el in field]
