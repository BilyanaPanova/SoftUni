# ROWS = 8
# COLUMNS = 8
#
#
# def find_players():
#     white_p = []
#     black_p = []
#     for r in range(ROWS):
#         for c in range(COLUMNS):
#             if play_ground[r][c] == "w":
#                 white_p.extend([r, c])
#             elif play_ground[r][c] == "b":
#                 black_p.extend([r, c])
#     return white_p, black_p
#
#
# def check_diagonals(args):
#     directions = {"left up": [-1, -1], "left down": [1, -1], "right up": [-1, 1], "right down": [1, 1]}
#     for d in directions.keys():
#
#         r, c = [x + y for x, y in zip(args, directions[d])]
#         if r in range(ROWS) and c in range(COLUMNS):
#             if play_ground[r][c] != "-":
#                 return True
#     return False
#
#
# def white_move(playground, *args):
#     if check_diagonals(args):
#         return f"Game over! White win, capture on {board[black_pawn[0]][black_pawn[1]]}."
#     r, c = args[0] - 1, args[1]
#     if r != 0 and c in range(COLUMNS):
#         playground[r][c] = "w"
#         playground[args[0]][args[1]] = "-"
#         return playground
#     return f"Game over! White pawn is promoted to a queen at {board[r][c]}."
#
#
# def black_move(playground, *args):
#     if check_diagonals(args):
#         return f"Game over! Black win, capture on {board[white_pawn[0]][white_pawn[1]]}."
#     r, c = args[0] + 1, args[1]
#     if r != 7 and c in range(COLUMNS):
#         playground[r][c] = "b"
#         playground[args[0]][args[1]] = "-"
#         return playground
#     return f"Game over! Black pawn is promoted to a queen at {board[r][c]}."
#
#
# board = []
# for row in range(ROWS):
#     board.append([str(ROWS - row) for x in range(COLUMNS)])
#     for col in range(COLUMNS):
#         board[row][col] = chr(97 + col) + board[row][col]
#
# play_ground = [input().split() for _ in range(ROWS)]
# counter = 1
# while True:
#     try:
#         white_pawn, black_pawn = find_players()
#     except IndexError:
#         print(play_ground)
#         break
#     if counter % 2 != 0:
#         play_ground = white_move(play_ground, *white_pawn)
#     else:
#         play_ground = black_move(play_ground, *black_pawn)
#     counter += 1
#
#

SIZE = 8


def find_players():
    white_p = []
    black_p = []
    for r in range(SIZE):
        for c in range(SIZE):
            if play_ground[r][c] == "w":
                white_p.extend([r, c])
            elif play_ground[r][c] == "b":
                black_p.extend([r, c])
    return white_p, black_p


def check_diagonals(args):
    directions = {"left up": [-1, -1], "left down": [1, -1], "right up": [-1, 1], "right down": [1, 1]}
    for d in directions.keys():
        r, c = [x + y for x, y in zip(args, directions[d])]
        if r in range(SIZE) and c in range(SIZE):
            if play_ground[r][c] != "-":
                return r, c
    return False


def move(playground, *args):
    winner = "White" if counter % 2 == 0 else "Black"
    m = 1 if counter % 2 == 0 else -1
    r, c = args[0] - m, args[1]
    diagonals = check_diagonals(args)

    if diagonals:
        return f"Game over! {winner} win, capture on {chr(97 + diagonals[1]) + str(SIZE - diagonals[0])}."
    if r != 0 and r != 7:
        playground[r][c] = winner[0].lower()
        playground[args[0]][args[1]] = "-"
        return playground

    return f"Game over! {winner} pawn is promoted to a queen at {chr(97 + c) + str(SIZE - r)}."


play_ground = [input().split() for _ in range(SIZE)]
counter = 0
while True:

    try:
        white_pawn, black_pawn = find_players()
    except IndexError:
        print(play_ground)
        break

    player = white_pawn if counter % 2 == 0 else black_pawn
    play_ground = move(play_ground, *player)
    counter += 1
