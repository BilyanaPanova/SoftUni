from collections import deque

males = [int(x) for x in input().split()]
females = deque(int(x) for x in input().split())
matches = 0
while males and females:
    male = males.pop()
    female = females.popleft()

    if male <= 0:
        females.appendleft(female)
        continue
    if male % 25 == 0:
        females.appendleft(female)
        if males:
            males.pop()
        continue

    if female <= 0:
        males.append(male)
        continue

    if female % 25 == 0:
        males.append(male)
        if females:
            females.popleft()
        continue

    if male == female:
        matches += 1
    else:
        male -= 2
        males.append(male)

print(f"Matches: {matches}")
if not males:
    print("Males left: none")
else:
    print(f"Males left: {', '.join(map(str,males[::-1]))}")

if females:
    print(f"Females left: {', '.join(map(str,females))}")
else:
    print("Females left: none")