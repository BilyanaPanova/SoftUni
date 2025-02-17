animals = input().split(", ")
position_wolf = animals.index("wolf")

if position_wolf == len(animals) - 1:
    print("Please go away and stop eating my sheep")
else:
    sheep = len(animals[:position_wolf:-1])
    print(f"Oi! Sheep number {sheep}! You are about to be eaten by a wolf!")
