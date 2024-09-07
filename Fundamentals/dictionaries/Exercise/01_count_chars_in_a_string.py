from collections import Counter

string = input()
string = string.replace(" ", "")
dict_string = Counter(string)

for key, value in dict_string.items():
    print(f"{key} -> {value}")

