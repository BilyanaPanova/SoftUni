import re

input_string = input()
all_numbers = []

while input_string:
    pattern = r"\d+"
    numbers_from_string = re.findall(pattern, input_string)

    if numbers_from_string:
        print(*numbers_from_string, end=" ")

    input_string = input()
