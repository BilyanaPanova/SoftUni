def is_reach_request():
    if resource_dict["shards"] >= 250:
        print(f"Shadowmourne obtained!")
        resource_dict["shards"] -= 250
        return True
    elif resource_dict["fragments"] >= 250:
        print("Valanyr obtained!")
        resource_dict["fragments"] -= 250
        return True
    elif resource_dict["motes"] >= 250:
        print("Dragonwrath obtained!")
        resource_dict["motes"] -= 250
        return True


resource_dict = {
    "shards": 0,
    "fragments": 0,
    "motes": 0
                 }

flag = True

while flag:
    input_line = input().split()

    for index in range(1, len(input_line), 2):
        material = input_line[index].lower()
        quantity = int(input_line[index-1])

        if material not in resource_dict:
            resource_dict[material] = 0
        resource_dict[material] += quantity

        if is_reach_request():
            flag = False
            break

for key, value in resource_dict.items():
    print(f"{key}: {value}")


# 2
# items = {"shards": 0, "fragments": 0, "motes": 0}
# winner = ""
#
# while not winner:
#     information = input().split()
#
#     for index in range(0, len(information), 2):
#         value = int(information[index])
#         key = information[index + 1].lower()
#
#         if key not in items.keys():
#             items[key] = 0
#         items[key] += value
#
#         if items["shards"] >= 250:
#             winner = "Shadowmourne"
#         elif items["fragments"] >= 250:
#             winner = "Valanyr"
#         elif items["motes"] >= 250:
#             winner = "Dragonwrath"
#
#         if winner:
#             print(f"{winner} obtained!")
#             items = {key: value - 250 if value >= 250 and key in ("shards", "fragments", "motes") else value for
#                      key, value in items.items()}
#             break
#
# for material, quantity in items.items():
#     print(f"{material}: {quantity}")
