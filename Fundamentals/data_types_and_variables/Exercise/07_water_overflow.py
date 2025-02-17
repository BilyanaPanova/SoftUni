input_lines = int(input())
capacity_tank = 255
litters_in_the_tank = 0

for _ in range(input_lines):
    litters_of_water = int(input())

    if litters_of_water > capacity_tank:
        print("Insufficient capacity!")
        continue

    capacity_tank -= litters_of_water
    litters_in_the_tank += litters_of_water

print(litters_in_the_tank)
