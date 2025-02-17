dict_with_information = {}
entry = input()

while entry != "end":
    name, command = entry.split(" = ")

    if command.isdigit():
        command = int(command)
    elif command in dict_with_information.keys():
        command = dict_with_information[command]
    else:
        entry = input()
        continue

    if name not in dict_with_information:
        dict_with_information[name] = 0

    dict_with_information[name] = command
    entry = input()

for key, value in dict_with_information.items():
    print(f"{key} === {value}")
