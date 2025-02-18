import re

some_string = input()

pattern = r"(0x)?[0-9A-F]+\b"
matches = re.finditer(pattern, some_string)

for match in matches:
    print(match.group(), end=" ")
