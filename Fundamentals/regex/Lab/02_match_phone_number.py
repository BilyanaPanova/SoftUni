import re

input_string = input()
match = re.findall(r"\+359 2 \d{3} \d{4}|\+359-2-\d{3}-\d{4}\b", input_string)
print(*match, sep=", ")
