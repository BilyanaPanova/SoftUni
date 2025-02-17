# size = int(input())
# all_moves = input().split(", ")
# squirrel_position = []
# field = []
# hazelnuts = []
# for row in range(size):
#     field.append(list(input()))
#     for col in range(size):
#         if field[row][col] == "s":
#             squirrel_position = [row, col]
#         elif field[row][col] == "h":
#             hazelnuts.append([row, col])
#
# moves = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}
#
# for move in all_moves:
#     r, c = [x + y for x, y in zip(squirrel_position, moves[move])]
#     squirrel_position = [r, c]
#     if [r, c] in hazelnuts:
#         hazelnuts.remove([r, c])
#
#     if not hazelnuts:
#         print("Good job! You have collected all hazelnuts!")
#         break
#
#     if r in range(size) and c in range(size):
#         if field[r][c] == "t":
#             print("Unfortunately, the squirrel stepped on a trap...")
#             break
#     else:
#         print("The squirrel is out of the field.")
#         break
#
# else:
#     print("There are more hazelnuts to collect.")
#
# print(f"Hazelnuts collected: {3 - len(hazelnuts)}")


size = int(input())
all_moves = input().split(", ")
squirrel_position = []
field = []

for row in range(size):
    line = (list(input()))
    field.append(line)

    if "s" in line:
        squirrel_position = [row, line.index("s")]

moves = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}
hazelnut_count = 0

for move in all_moves:
    r, c = [x + y for x, y in zip(squirrel_position, moves[move])]
    squirrel_position = [r, c]

    if r in range(size) and c in range(size):

        if field[r][c] == "h":
            hazelnut_count += 1
            field[r][c] = "*"
        elif field[r][c] == "t":
            print("Unfortunately, the squirrel stepped on a trap...")
            break

        if hazelnut_count == 3:
            print("Good job! You have collected all hazelnuts!")
            break

    else:
        print("The squirrel is out of the field.")
        break

else:
    print("There are more hazelnuts to collect.")

print(f"Hazelnuts collected: {hazelnut_count}")
