numbers_of_intput_line = int(input())
matrix = [input().split() for _ in range(numbers_of_intput_line)]
directions = [(0, - 1), (0, 1), (1, 0), (-1, 0)]
dot = "."
dashes = "-"
all_moves = []
while True:
    dot_position = [[x, y.index(dot)] for x, y in enumerate(matrix) if dot in y]
    if dot_position:
        dot_row,dot_col = dot_position[0][0],dot_position[0][1]
        matrix[dot_row][dot_col] = "m"
        moves = 1
        while True:
            for r, c in directions:
                new_row, new_col = dot_row + r, dot_col + c
                if new_col in range(len(matrix[dot_row])) and new_row in range(len(matrix)):
                    if matrix[new_row][new_col] == dot:
                        moves += 1
                        matrix[new_row][new_col] = "m"
                        row, col = new_row, new_col
                        break
                    if matrix[new_row][new_col] == "m":
                        row, col = new_row, new_col
                        continue
            else:
                break
        all_moves.append(moves)
    else:
        break

print(all_moves)
