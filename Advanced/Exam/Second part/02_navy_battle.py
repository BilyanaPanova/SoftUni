size = int(input())


def create_matrix():
    board = []
    start_position = []
    cruisers_position = []
    for r in range(size):
        board.append(list(input()))
        for c in range(size):
            if board[r][c] == "S":
                start_position.extend([r, c])
            elif board[r][c] == "C":
                cruisers_position.append([r, c])
    return board, start_position, cruisers_position


field, position, cruisers = create_matrix()
mines_counter = 0
directions = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}

while cruisers and mines_counter < 3:
    direction = input()

    field[position[0]][position[1]] = "-"
    row, col = [x + y for x, y in zip(position, directions[direction])]
    if row in range(size) and col in range(size):
        if field[row][col] == "*":
            mines_counter += 1
        elif field[row][col] == "C":
            cruisers.remove([row, col])

        field[row][col] = "S"
        position = [row, col]

if cruisers:
    print(f"Mission failed, U-9 disappeared! Last known coordinates [{position[0]}, {position[1]}]!")
else:
    print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
[print(*el,sep="") for el in field]