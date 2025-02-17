import re

names = input()
match = re.findall(r"\b[A-Z][a-z]+ [A-Z][a-z]+\b", names)
print(*match)
