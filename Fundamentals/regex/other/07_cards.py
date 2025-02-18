import re

some_string = input()

pattern = r"[23456789JQKA]{1}[SHDC]|10[SHDC]"
match = re.findall(pattern, some_string)

print(*match, sep=" ")
