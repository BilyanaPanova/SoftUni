del_string = input()
string = input()

while del_string in string:
    string = string.replace(del_string, "")

print(string)
