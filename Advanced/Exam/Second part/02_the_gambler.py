size = int(input())
amount = 100
position = []
board = []
for row in range(size):
    line = list(input())
    if "G" in line:
        position.extend([row, line.index("G")])
    board.append(line)
direction_mapper = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}
while amount > 0:
    command = input()
    if command == "end":
        print(f"End of the game. Total amount: {amount}$")
        break
    board[position[0]][position[1]] = "-"
    curr_row, curr_col = [x + y for x, y in zip(position, direction_mapper[command])]
    if curr_row in range(size) and curr_col in range(size):
        position = [curr_row, curr_col]
        symbol_ = board[curr_row][curr_col]
        board[curr_row][curr_col] = "G"
        if symbol_ == "W":
            amount += 100
        elif symbol_ == "P":
            amount -= 200
        elif symbol_ == "J":
            amount += 100000
            print(f"You win the Jackpot!\nEnd of the game. Total amount: {amount}$")
            break
    else:
        amount = 0
else:
    print("Game over! You lost everything!")

if amount > 0:
    [print(*el, sep="") for el in board]
