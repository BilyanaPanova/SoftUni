def registration_to_enter(my_dict, name, license_plate):
    if name in my_dict:
        plate_number = my_dict.get(name)
        return f"ERROR: already registered with plate number {plate_number}"
    else:
        my_dict[name] = license_plate
        return f"{name} registered {license_plate} successfully"


def unregister_to_leave(my_dict, name):
    if name not in my_dict:
        return f"ERROR: user {name} not found"
    else:
        del my_dict[name]
        return f"{name} unregistered successfully"


parking_dict = {}
count_of_input_line = int(input())
for _ in range(count_of_input_line):
    command = input().split()
    action = command[0]
    username = command[1]

    if action == "register":
        license_plate_number = command[2]
        print(registration_to_enter(parking_dict, username, license_plate_number))
    elif action == "unregister":
        print(unregister_to_leave(parking_dict, username))

for name,number in parking_dict.items():
    print(f"{name} => {number}")
