dict_of_all_resource = {}
while True:
    command = input()

    if command == "stop":
        for key, value in dict_of_all_resource.items():
            print(f"{key} -> {value}")
        break

    resource = command
    quantity = int(input())
    if resource not in dict_of_all_resource:
        dict_of_all_resource[resource] = 0
    dict_of_all_resource[resource] += quantity

