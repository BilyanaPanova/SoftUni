some_string = input()
size_matrix = int(input())
matrix = []
position = []

for i in range(size_matrix):
    line = list(input())
    matrix.append(line)
    if "P" in line:
        position.extend([i, line.index("P")])

directions = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}

for _ in range(int(input())):
    command = input()

    curr_r, curr_c = [x + y for x, y in zip(position, directions[command])]
    if curr_r in range(size_matrix) and curr_c in range(size_matrix):
        if matrix[curr_r][curr_c].isalpha():
            some_string += matrix[curr_r][curr_c]
        matrix[position[0]][position[1]] = "-"
        position = [curr_r, curr_c]
        matrix[curr_r][curr_c] = "P"
    else:
        some_string = some_string[:-1]

print(some_string)
[print(*el, sep="") for el in matrix]
