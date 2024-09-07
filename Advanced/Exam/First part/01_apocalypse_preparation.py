from collections import deque

textiles = deque(int(x) for x in input().split())
medicaments = [int(x) for x in input().split()]

healing_items = {40: ["Bandage", 0], 100: ["MedKit", 0],30: ["Patch", 0]}

while textiles and medicaments:
    textile = textiles.popleft()
    medicament = medicaments.pop()
    curr_sum = textile + medicament
    if curr_sum in healing_items.keys():
        healing_items[curr_sum][1] += 1
    elif curr_sum > 100:
        healing_items[100][1] += 1
        medicaments[-1] += curr_sum - 100
    else:
        medicaments.append(medicament + 10)

if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")
elif not textiles:
    print("Textiles are empty.")
elif not medicaments:
    print("Medicaments are empty.")

for item, count in sorted(healing_items.values(), key=lambda x: -x[1]):
    if count != 0:
        print(f"{item} - {count}")

if medicaments:
    print(f"Medicaments left: {', '.join(map(str, reversed(medicaments)))}")
if textiles:
    print(f"Textiles left: {', '.join(map(str, textiles))}")
