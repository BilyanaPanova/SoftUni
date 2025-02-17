def position_snake():
    position = [[row, col] for row in range(len(field)) for col in range(len(field)) if field[row][col] == "S"]
    return position[0]


def position_burrow():
    position = [[row, col] for row in range(len(field)) for col in range(len(field)) if field[row][col] == "B"]
    return position


field = [list(input()) for y in range(int(input()))]
burrows = position_burrow()
directions = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}
food_counter = 0
while True:
    snake = position_snake()
    curr_r, curr_c = [x + y for x, y in zip(snake, directions[input()])]
    if curr_c in range(len(field)) and curr_r in range(len(field)):
        if field[curr_r][curr_c] == "*":
            food_counter += 1
        elif field[curr_r][curr_c] == "B":
            field[curr_r][curr_c] = "."
            burrows.remove([curr_r, curr_c])
            curr_r, curr_c = burrows.pop()
        field[snake[0]][snake[1]] = "."
        field[curr_r][curr_c] = "S"
    else:
        print("Game over!")
        field[snake[0]][snake[1]] = "."
        break

    if food_counter == 10:
        print("You won! You fed the snake.")
        break
print(f"Food eaten: {food_counter}")
[print(*el, sep="") for el in field]
