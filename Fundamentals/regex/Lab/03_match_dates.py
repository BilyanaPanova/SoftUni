import re

string_of_dates = input()

pattern = r"\b(?P<Day>[0-9]{2})([./-])(?P<Month>[A-Z][a-z]{2})\2(?P<Year>[0-9]{4})\b"
matches = re.findall(pattern, string_of_dates)

for match in matches:
    day = match[0]
    month = match[2]
    year = match[3]
    print(f"Day: {day}, Month: {month}, Year: {year}")
