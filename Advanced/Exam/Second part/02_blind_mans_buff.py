rows, columns = [int(x) for x in input().split()]
position = []
matrix = []
other_players = []
made_moves = 0
for row in range(rows):
    matrix.append(input().split())
    for column in range(columns):
        if matrix[row][column] == "B":
            position = [row, column]
        elif matrix[row][column] == "P":
            other_players.append([row, column])
directions = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}
while True:
    command = input()
    if command == "Finish" or not other_players:
        print(f"Game over!\nTouched opponents: {3 - len(other_players)} Moves made: {made_moves}")
        break
    new_row, new_col = [x + y for x, y in zip(directions[command], position)]
    if new_row in range(rows) and new_col in range(columns):
        if [new_row, new_col] in other_players:
            other_players.remove([new_row, new_col])
        if matrix[new_row][new_col] != "O":
            matrix[position[0]][position[1]] = "-"
            position = [new_row, new_col]
            made_moves += 1