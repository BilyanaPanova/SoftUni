import re

sequence_of_numbers = input()

pattern = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"
matches = re.finditer(pattern, sequence_of_numbers)

for mach_number in matches:
    print(mach_number.group(), end=" ")
