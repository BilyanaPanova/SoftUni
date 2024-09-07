import re

string = input()

list_of_chars = re.findall(r"\D+", string)
list_of_digit = re.findall(r"\d+", string)
new_string_list = [x.upper() * int(y) for x, y in zip(list_of_chars, list_of_digit)]
new_string = "".join(new_string_list)
number_of_unique_symbols = len(set(new_string))

print(f"Unique symbols used: {number_of_unique_symbols}")
print(new_string)
