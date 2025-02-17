from collections import deque

fireworks = {"Palm Fireworks": 0, "Willow Fireworks": 0, "Crossette Fireworks": 0}

effects = deque(int(x) for x in input().split(", "))
power = deque(int(x) for x in input().split(", "))

while effects and power:
    if effects[0] <= 0 or power[-1] <= 0:
        if effects[0] <= 0:
            effects.popleft()
        if power[-1] <= 0:
            power.pop()
        continue

    curr_effect = effects.popleft()
    curr_power = power.pop()
    curr_sum = curr_power + curr_effect

    if curr_sum % 3 == 0 and curr_sum % 5 == 0:
        fireworks["Crossette Fireworks"] += 1
    elif curr_sum % 3 == 0 and curr_sum % 5 != 0:
        fireworks["Palm Fireworks"] += 1
    elif curr_sum % 3 != 0 and curr_sum % 5 == 0:
        fireworks["Willow Fireworks"] += 1
    else:
        effects.append(curr_effect - 1)
        power.append(curr_power)

    prepared_fireworks = [x for x in fireworks.values() if x >= 3]

    if len(prepared_fireworks) == 3:
        print("Congrats! You made the perfect firework show!")
        break

else:
    print("Sorry. You can't make the perfect firework show.")

if effects:
    print(f"Firework Effects left: {', '.join(map(str, effects))}")

if power:
    print(f"Explosive Power left: {', '.join(map(str, power))}")

for key, value in fireworks.items():
    print(f"{key}: {value}")
