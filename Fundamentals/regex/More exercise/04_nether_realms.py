import re

names = [x.strip() for x in input().split(",")]
pattern_health = r"[^0-9\+\-\*\/\.]"
pattern_damage = r'((-)?\d+(?:\.\d+)?)'
demons_info = {}

for name in names:
    find_heal_char = re.findall(pattern_health, name)
    total_health = sum([ord(x) for x in find_heal_char])

    find_damage_char = re.findall(pattern_damage, name)
    total_damage = sum([float(x[0]) for x in find_damage_char])

    if "*" in name:
        count = name.count("*")
        for _ in range(count):
            total_damage *= 2

    if "/" in name:
        count = name.count("/")
        for _ in range(count):
            total_damage /= 2

    demons_info[name] = {"Health": total_health, "Damage": total_damage}

for demons, info in sorted(demons_info.items()):
    print(f"{demons} - {demons_info[demons]['Health']} health, {demons_info[demons]['Damage']:.2f} damage")
