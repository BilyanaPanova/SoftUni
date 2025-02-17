def input_information():
    matrix, count_cheese, start_position = [], 0, []
    for row in range(rows):
        line = list(input())
        matrix.append(line)
        if "M" in line:
            start_position = [row, line.index("M")]
        if "C" in line:
            count_cheese += line.count("C")
    return start_position, count_cheese, matrix


def find_cheese():
    global board
    global cheese

    cheese -= 1
    if cheese == 0:
        return "Happy mouse! All the cheese is eaten, good night!"
    return ""


def trapped():
    return "Mouse is trapped!"


def star_position():
    return ""


rows, columns = (int(x) for x in input().split(","))
position, cheese, field = input_information()
moves = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}
mapper = {"C": find_cheese, "T": trapped, "*": star_position}
result = ""
while not result:
    command = input()

    try:
        row, col = [x + y for x, y in zip(position, moves[command])]
        curr_symbol = field[row][col]
    except IndexError:
        result = "No more cheese for tonight!"
        break
    except KeyError:
        result = "Mouse will come back later!"
        break

    if curr_symbol in mapper:
        result = mapper[curr_symbol]()
        field[position[0]][position[1]] = "*"
        field[row][col] = "M"
        position = [row, col]

print(result)
[print(*el, sep="") for el in field]
