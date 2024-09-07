number_of_decoration = int(input())
days = int(input())
christmas_spirit = 0
total = 0
if days % 10 == 0:
    christmas_spirit -= 30
for day in range(1, days + 1):
    if day % 11 == 0:
        number_of_decoration += 2
    if day % 2 == 0:
        total += number_of_decoration * 2
        christmas_spirit += 5
    if day % 3 == 0:
        total += number_of_decoration * 8
        christmas_spirit += 13
    if day % 5 == 0:
        total += number_of_decoration * 15
        christmas_spirit += 17
    if day % 10 == 0:
        christmas_spirit -= 20
        total += 23
    if day % 3 == 0 and day % 5 == 0:
        christmas_spirit += 30
print(f"Total cost: {total}")
print(f"Total spirit: {christmas_spirit}")
