def is_valid(password):
    flag = True
    if len(password) not in range(6,11):
        print("Password must be between 6 and 10 characters")
        flag = False
    if not password.isalnum():
        print("Password must consist only of letters and digits")
        flag = False
    if len([x for x in password if x.isdigit()]) < 2:
        print("Password must have at least 2 digits")
        flag = False
    if flag:
        print("Password is valid")


password = input()
is_valid(password)
