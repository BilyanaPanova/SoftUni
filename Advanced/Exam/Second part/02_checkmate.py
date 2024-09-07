field = [input().split() for _ in range(8)]

find_king = [[r, c] for c in range(8) for r in range(8) if field[r][c] == "K"][0]
directions = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1], "left up": [-1, -1],
              "left down": [1, -1], "right up": [-1, 1], "right down": [1, 1]}

queens = []
for direction in directions.values():
    row, col = find_king
    row += direction[0]
    col += direction[1]
    while row in range(8) and col in range(8):
        if field[row][col] == "Q":
            queens.append([row, col])
            break
        row += direction[0]
        col += direction[1]

if queens:
    print(*queens, sep="\n")
else:
    print("The king is safe!")
