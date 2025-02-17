size = int(input())
matrix = [input().split() for _ in range(size)]
directions = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}
path = []
points = 0
while True:
    command = input()
    player = [[x, y] for x in range(size) for y in range(size) if matrix[x][y] == "P"]
    path.append(*player)
    if command in directions.keys():
        curr_r, curr_c = [x + y for x, y in zip(*player, directions[command])]
        if curr_r not in range(size) or curr_c not in range(size):
            if curr_r >= size:
                curr_r = 0
            elif curr_r < 0:
                curr_r = size - 1
            if curr_c >= size:
                curr_c = 0
            elif curr_c < 0:
                curr_c = size - 1

        if matrix[curr_r][curr_c].isdigit():
            points += int(matrix[curr_r][curr_c])
        else:
            path.append([curr_r, curr_c])
            print(f"Game over! You've collected {points // 2} coins.")
            break
        matrix[player[0][0]][player[0][1]] = "0"
        matrix[curr_r][curr_c] = "P"

    if points >= 100:
        path.append([curr_r, curr_c])
        print(f"You won! You've collected {points} coins.")
        break
print(f"Your path:")
print('\n'.join(map(str, path)))
