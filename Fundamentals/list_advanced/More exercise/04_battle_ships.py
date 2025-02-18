number_of_inputs = int(input())
ships = [list(int(x) for x in input().split()) for _ in range(number_of_inputs)]
attack_coordinate = input().split()
destroyed_ships = 0

for current_coordinate in attack_coordinate:
    row, col = current_coordinate.split("-")
    row, col = int(row), int(col)
    ships[row][col] -= 1
    if ships[row][col] == 0:
        destroyed_ships += 1

print(destroyed_ships)