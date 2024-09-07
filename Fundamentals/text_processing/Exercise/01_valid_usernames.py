import string


def valid_length(name_):
    if len(name_) in range(3, 17):
        return True
    return False


def valid_simbols(name_):
    list_of_valid_simbols = list(string.ascii_letters + string.digits + "-" + "_")
    is_valid = all([True if x in list_of_valid_simbols else False for x in name_])
    return is_valid


usernames = input().split(", ")

for name in usernames:
    if valid_length(name) and valid_simbols(name):
        print(name)
