number_of_inputs = int(input())
maze = [list(input()) for _ in range(number_of_inputs)]
wall = "#"
empty_space = " "
position_k = "k"

moves = 1
start_position = [[x, y.index(position_k)] for x, y in enumerate(maze) if position_k in y]
row, col = start_position[0][0], start_position[0][1]
directions = [(0, - 1), (0, 1), (1, 0), (-1, 0)]
while True:

    for r, c in directions:
        new_row, new_col = row + r, col + c
        if new_col in range(len(maze[row])) and new_row in range(len(maze)):
            if maze[new_row][new_col] == empty_space:
                moves += 1
                maze[new_row][new_col] = position_k
                row, col = new_row, new_col
                break

    else:
        if row == len(maze) - 1 or row == 0 or col == 0 or col == len(maze[row])-1:
            print(f"Kate got out in {moves} moves")
        else:
            print("Kate cannot get out")
        break
