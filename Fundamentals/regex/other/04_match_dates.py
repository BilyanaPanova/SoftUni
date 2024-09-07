import re

some_dates = input()

pattern = r"(\d{2})([\.\-\/])([A-Z][a-z]{2})\2(\d{4})"
matches = re.finditer(pattern, some_dates)

for match in matches:
    print(f"Day: {match[1]}, Month: {match[3]}, Year: {match[4]}")
