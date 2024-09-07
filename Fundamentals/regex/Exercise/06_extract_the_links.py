import re

input_line = input()
pattern = r"www.[A-Za-z0-9\-\.]+\.[a-z]+"

while input_line:
    match = re.findall(pattern, input_line)

    if match:
        print(*match)

    input_line = input()
