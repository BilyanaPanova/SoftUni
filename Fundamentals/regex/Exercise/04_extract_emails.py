import re

some_string = input()

pattern = r"\s(\b[a-z0-9]+[a-z0-9\.\-\_]+@[a-z\-]+.[a-z]+\.[a-z]+?\b)"
matches = re.findall(pattern, some_string)

print(*matches, sep="\n")
