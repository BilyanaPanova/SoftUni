import re

some_string = input()
searched_word = input()

matches = re.findall(fr"(?i)\b{searched_word}\b", some_string)

print(len(matches))