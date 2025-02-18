size = int(input())
armor = 300
enemy = 4
direction_mapper = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}
position = []
field = []

for row in range(size):
    line = list(input())
    if "J" in line:
        position.extend([row,line.index("J")])
        line[line.index("J")] = "-"
    field.append(line)

while enemy != 0:
    move = input()
    curr_row,curr_col = [x+y for x,y in zip(direction_mapper[move],position)]
    mark = field[curr_row][curr_col]
    field[curr_row][curr_col] = "-"
    position = [curr_row, curr_col]
    if mark == "E":
        enemy -= 1
        armor -= 100
        if armor == 0:
            print(f"Mission failed, your jetfighter was shot down! Last coordinates [{position[0]}, {position[1]}]!")
            break

    elif mark == "R":
        armor = 300

else:
    print("Mission accomplished, you neutralized the aerial threat!")
field[position[0]][position[1]] = "J"
[print(*el,sep="") for el in field]
