gifts = input().split()
commands = input()

while commands != "No Money":
    commands = commands.split()
    detail = commands[0]

    if detail == "OutOfStock":
        gift = commands[1]
        gifts = ["None" if x == gift else x for x in gifts]
    elif detail == "Required":
        gift = commands[1]
        index = int(commands[2])
        if index in range(len(gifts)):
            gifts.pop(index)
            gifts.insert(index, gift)
    elif detail == "JustInCase":
        gift = commands[1]
        gifts[-1] = gift

    commands = input()

gifts = [x for x in gifts if x != "None"]

print(*gifts)
