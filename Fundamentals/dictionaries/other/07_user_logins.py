user_passwords = {}

while True:
    command = input()

    if command == "login":
        break

    username, password = command.split(" -> ")

    if username not in user_passwords:
        user_passwords[username] = ""

    user_passwords[username] = password


failed_passwords = 0

while True:
    another_command = input()

    if another_command == "end":
        break

    name, try_pass = another_command.split(" -> ")

    if name not in user_passwords.keys() or try_pass not in user_passwords.values():
        print(f"{name}: login failed")
        failed_passwords += 1
    else:
        print(f"{name}: logged in successfully")

print(f"unsuccessful login attempts: {failed_passwords}")
