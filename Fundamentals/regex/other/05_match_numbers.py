import re

some_numbers = input()

pattern = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"
matches = re.finditer(pattern, some_numbers)

for match in matches:
    print(match.group(), end=" ")
