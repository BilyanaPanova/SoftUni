def get_information(rows, columns):
    position = []
    workshop_dict = {"D": 0, "G": 0, "C": 0}
    matrix = []
    for r in range(rows):
        matrix.append(input().split())
        for c in range(columns):
            if matrix[r][c] in workshop_dict.keys():
                workshop_dict[matrix[r][c]] += 1
            elif matrix[r][c] == "Y":
                position.extend([r, c])
    return position, workshop_dict, matrix


def valid_range(value, matrix_range):
    if value >= matrix_range:
        value = 0
    elif value < 0:
        value = matrix_range - 1
    return value


def move(position, field_p, items):
    directions = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}

    for _ in range(int(steps)):
        row, col = [x + y for x, y in zip(position, directions[command])]
        curr_row = valid_range(row, ROWS)
        curr_col = valid_range(col, COLUMNS)

        if field_p[curr_row][curr_col] in items.keys():
            items[field_p[curr_row][curr_col]] += 1

        field_p[curr_row][curr_col] = "Y"
        field_p[position[0]][position[1]] = "x"
        position = [curr_row, curr_col]

        if sum(workshop.values()) == sum(items.values()):
            print("Merry Christmas!")
            return None, items

    return position, items


ROWS, COLUMNS = [int(x) for x in input().split(", ")]
start_position, workshop, field = get_information(ROWS, COLUMNS)
collected_items = {"D": 0, "G": 0, "C": 0}
while start_position:
    commands = input()
    if commands == "End":
        break
    command, steps = commands.split("-")
    start_position, collected_items = move(start_position, field, collected_items)


print("You've collected:")
print(f"- {collected_items['D']} Christmas decorations")
print(f"- {collected_items['G']} Gifts")
print(f"- {collected_items['C']} Cookies")
[print(*el, sep=" ") for el in field]
