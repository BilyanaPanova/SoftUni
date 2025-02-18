import re

pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"
some_string = input()
match = re.findall(pattern, some_string)
print(*match)


# match = re.findall(r"\b[A-Z][a-z]+ [A-Z][a-z]+\b",input())
# print(*match)
