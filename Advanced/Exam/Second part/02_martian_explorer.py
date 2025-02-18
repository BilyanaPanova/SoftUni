def find_e_position():
    e = [[row, col] for col in range(COLUMNS) for row in range(ROWS) if matrix[row][col] == "E"]
    return e[0]


def validate_position(value, range_p):
    if value >= range_p:
        value = 0
    else:
        value = range_p - 1
    return value


def current_position(direction):
    row, col = [x + y for x, y in zip(explorer, COMMANDS[direction])]
    if row in range(ROWS) and col in range(COLUMNS):
        return row, col
    if row not in range(ROWS):
        row = validate_position(row, ROWS)
    if col not in range(COLUMNS):
        col = validate_position(col, COLUMNS)
    return row, col


ROWS = 6
COLUMNS = 6
COMMANDS = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}
find_marking = {"W": 0, "M": 0, "C": 0}
matrix = [input().split() for _ in range(ROWS)]
explorer = find_e_position()
input_commands = input().split(", ")
for command in input_commands:
    r, c = current_position(command)
    if matrix[r][c] == "W":
        find_marking["W"] += 1
        print(f"Water deposit found at ({r}, {c})")
    elif matrix[r][c] == "M":
        find_marking["M"] += 1
        print(f"Metal deposit found at ({r}, {c})")
    elif matrix[r][c] == "C":
        find_marking["C"] += 1
        print(f"Concrete deposit found at ({r}, {c})")
    elif matrix[r][c] == "R":
        print(f"Rover got broken at ({r}, {c})")
        break
    explorer = [r,c]

marking = len([1 for x in find_marking.values() if x > 0])
if marking == 3:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
