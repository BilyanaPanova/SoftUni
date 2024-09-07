level_of_fire = input().split("#")
amount_of_water = int(input())


def is_in_range(type_of_fire, value):
    flag = True
    if type_of_fire == "High" and value in range(81, 126):
        pass
    elif type_of_fire == "Medium" and value in range(51, 81):
        pass
    elif type_of_fire == "Low" and value in range(1, 51):
        pass
    else:
        flag = False
    return flag


total_fire = 0
cells = []

for cell in level_of_fire:
    cell = cell.split(" = ")
    type_of_fire = cell[0]
    value = int(cell[1])

    if is_in_range(type_of_fire, value):
        if value > amount_of_water:
            continue
        total_fire += value
        amount_of_water -= value
        cells.append(value)

print("Cells:")
for el in cells:
    print(f" - {el}")
effort = total_fire * 0.25
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
