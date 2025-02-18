import re

some_numbers = input()

pattern = r"\+359([ -])2{1}(\1)\d{3}(\1)\d{4}\b"
matches = re.finditer(pattern, some_numbers)

for match in matches:
    print(match.group(), end=" ")
