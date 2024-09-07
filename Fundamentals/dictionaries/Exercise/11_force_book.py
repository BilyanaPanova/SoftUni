def add_force_user(my_dict, side, user):
    flag = [key for key, val in my_dict.items() if user in val]
    if side not in my_dict and not flag:
        my_dict[side] = [user]
    elif side in my_dict and not flag:
        my_dict[side].append(user)


def change_side(my_dict, user, side):
    for key, values in my_dict.items():
        if user in values:
            values.remove(user)
    if side not in my_dict:
        my_dict[side] = []
    my_dict[side].append(user)
    return f"{user} joins the {side} side!"


force_book = {}
while True:
    command = input()

    if command == "Lumpawaroo":
        for force, names in force_book.items():
            if len(names) > 0:
                print(f"Side: {force}, Members: {len(names)}")
                print(f"! " + "\n! ".join(names))
        break

    if "|" in command:
        force_side, username = command.split(" | ")
        add_force_user(force_book, force_side, username)
    elif "->" in command:
        username, force_side = command.split(" -> ")
        print(change_side(force_book, username, force_side))
