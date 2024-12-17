length = int(input())
width = int(input())
height = int(input())
occupied_space = float(input())

volume_fish_tank = length * width * height
volume_in_litters = volume_fish_tank * 0.001
needed_litters = volume_in_litters * (1 - (occupied_space / 100))

print(needed_litters)
