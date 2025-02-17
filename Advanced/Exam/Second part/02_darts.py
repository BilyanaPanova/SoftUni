import math


def is_digit(r, c):
    points = int(board[r][c])
    return points


def is_D(r, c):
    included_coordinate = (board[r][0], board[r][6], board[0][c], board[6][c])
    points = sum([int(x) for x in included_coordinate]) * 2
    return points


def is_T(r, c):
    included_coordinate = (board[r][0], board[r][6], board[0][c], board[6][c])
    points = sum([int(x) for x in included_coordinate]) * 3
    return points


def winner():
    for name, points in (first_player.values(), second_player.values()):
        if points <= 0:
            return name
    return None


first_player = {"name": "", "points": 501}
second_player = {"name": "", "points": 501}

first_player["name"], second_player["name"] = input().split(", ")

board = [input().split() for _ in range(7)]

coordinate = input()
count = 1
reduce_points = 0
while coordinate:
    row, col = [int(x) for x in coordinate.strip("()").split(", ")]
    if row in range(7) and col in range(7):
        if board[row][col].isdigit():
            reduce_points = is_digit(row, col)
        elif board[row][col] == "D":
            reduce_points = is_D(row, col)
        elif board[row][col] == "B":
            reduce_points = 501
        else:
            reduce_points = is_T(row, col)

        if count % 2 == 0:  # second_player
            second_player["points"] -= reduce_points
        else:               # first_player
            first_player["points"] -= reduce_points

        if winner():
            name = winner()
            count_turns = math.ceil(count / 2)
            print(f"{name} won the game with {count_turns} throws!")
            break
    count += 1
    coordinate = input()
