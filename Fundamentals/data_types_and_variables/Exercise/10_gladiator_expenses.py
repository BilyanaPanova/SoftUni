lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
broken_helmet = 0
broken_sword = 0
broken_shield = 0
broken_armor = 0

for second in range(1, lost_fights_count + 1):

    if second % 2 == 0:
        broken_helmet += 1
    if second % 3 == 0:
        broken_sword += 1
        if second % 2 == 0:
            broken_shield += 1
            if broken_shield % 2 == 0 and broken_shield != 0:
                broken_armor += 1

total = ((broken_shield * shield_price) +
         (broken_armor * armor_price) +
         (broken_helmet * helmet_price) +
         (broken_sword * sword_price))
print(f"Gladiator expenses: {total:.2f} aureus")
