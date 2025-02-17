from collections import deque

worms = [int(x) for x in input().split()]
holes = deque([int(x) for x in input().split()])
matches = 0
all_worms = len(worms)

while worms and holes:
    worm = worms.pop()
    hole = holes.popleft()

    if worm != hole:
        diff = worm - 3
        if diff > 0:
            worms.append(diff)
    else:
        matches += 1

if matches > 0:
    print(f"Matches: {matches}")
else:
    print("There are no matches.")

if all_worms == matches:
    print("Every worm found a suitable hole!")
elif worms:
    print(f"Worms left: {', '.join(map(str,worms))}")
else:
    print("Worms left: none")

if holes:
    print(f"Holes left: {', '.join(map(str,holes))}")
else:
    print("Holes left: none")
