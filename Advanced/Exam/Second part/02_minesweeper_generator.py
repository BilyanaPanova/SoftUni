n = int(input())

matrix = [[0 for x in range(n)] for y in range(n)]
directions = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1], "left up": [-1, -1],
              "left down": [1, -1], "right up": [-1, 1], "right down": [1, 1]}

for _ in range(int(input())):
    r, c = [int(x) for x in input().strip("()").split(", ")]
    matrix[r][c] = "*"

    for direction in directions:
        curr_r, curr_c = [x + y for x, y in zip((r, c), directions[direction])]
        if curr_r in range(n) and curr_c in range(n) and matrix[curr_r][curr_c] != "*":
            matrix[curr_r][curr_c] += 1

[print(*el, sep=" ") for el in matrix]
