size = int(input())
number = input()
matrix = []
tunnels = []
for row in range(size):
    matrix.append(input().split())
    for col in range(size):
        if matrix[row][col] == "T":
            tunnels.append([row, col])
start_position = [0, 0]
moves = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}
distance = 0
while True:
    command = input()
    if command == "End":
        print(f"Racing car {number} DNF.")
        break

    row, col = start_position[0] + moves[command][0], start_position[1] + moves[command][1]
    distance += 10
    matrix[start_position[0]][start_position[1]] = "."
    start_position = [row,col]

    if matrix[row][col] == "T":
        tunnels.remove([row, col])
        matrix[row][col] = "."
        start_position = tunnels[0]
        distance += 20
    elif matrix[row][col] == "F":
        print(f"Racing car {number} finished the stage!")
        break

print(f"Distance covered {distance} km.")
matrix[start_position[0]][start_position[1]] = "C"
[print(*el,sep="") for el in matrix]