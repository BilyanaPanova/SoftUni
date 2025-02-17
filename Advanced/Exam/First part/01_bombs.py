from collections import deque


def sum_bombs(a, b):
    return a + b


def add_bomb(effect, casing):
    while True:
        curr_value = sum_bombs(effect, casing)
        if curr_value in bombs.keys():
            bombs[curr_value][1] += 1
            break
        else:
            casing -= 5


effects = deque(int(x) for x in input().split(", "))
casings = deque(int(x) for x in input().split(", "))

bombs = {60: ["Cherry Bombs", 0], 40: ["Datura Bombs", 0], 120: ["Smoke Decoy Bombs", 0]}

while effects and casings:
    curr_effect = effects.popleft()
    curr_casing = casings.pop()

    add_bomb(curr_effect, curr_casing)
    fill_bombs = len([x[1] for x in bombs.values() if x[1] > 2]) == 3

    if fill_bombs:
        print("Bene! You have successfully filled the bomb pouch!")
        break
else:
    print("You don't have enough materials to fill the bomb pouch.")

if effects:
    print(f"Bomb Effects: {', '.join(map(str, effects))}")
else:
    print("Bomb Effects: empty")

if casings:
    print(f"Bomb Casings: {', '.join(map(str, casings))}")
else:
    print("Bomb Casings: empty")

[print(f"{x[0]}: {x[1]}") for x in bombs.values()]
