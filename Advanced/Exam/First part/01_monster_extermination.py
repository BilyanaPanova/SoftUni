from collections import deque

monsters = deque([int(x) for x in input().split(",")])
soldiers = [int(x) for x in input().split(",")]
all_monsters = len(monsters)

while monsters and soldiers:
    monster = monsters.popleft()
    soldier = soldiers.pop()

    if soldier > monster:
        add_value = soldier - monster
        if soldiers:
            soldiers[-1] += add_value
        else:
            soldiers.append(add_value)

    elif soldier < monster:
        monsters.append(monster - soldier)

if not monsters:
    print("All monsters have been killed!")

if not soldiers:
    print("The soldier has been defeated.")

print(f"Total monsters killed: {all_monsters - len(monsters)}")
