from collections import deque

materials = [int(x) for x in input().split()]
magics = deque(int(x) for x in input().split())

presents = {"Diamond Jewellery": 0, "Gemstone": 0, "Gold": 0, "Porcelain Sculpture": 0}

while materials and magics:
    curr_material = materials.pop()
    curr_magic = magics.popleft()
    curr_sum = curr_magic + curr_material

    if curr_sum < 100:
        if curr_sum % 2 == 0:
            curr_material *= 2
            curr_magic *= 3
            curr_sum = curr_material + curr_magic
        else:
            curr_sum *= 2

    if curr_sum > 499:
        curr_sum //= 2

    if curr_sum in range(100, 200):
        presents["Gemstone"] += 1
    elif curr_sum in range(200, 300):
        presents["Porcelain Sculpture"] += 1
    elif curr_sum in range(300, 400):
        presents["Gold"] += 1
    elif curr_sum in range(400, 500):
        presents["Diamond Jewellery"] += 1

if (presents["Gemstone"] and presents["Porcelain Sculpture"]) or (presents["Gold"] and presents["Diamond Jewellery"]):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join(map(str, materials))}")

if magics:
    print(f"Magic left: {', '.join(map(str, magics))}")

for key, value in presents.items():
    print(f"{key}: {value}") if value > 0 else None
