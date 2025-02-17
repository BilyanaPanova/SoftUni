import re

string = input().lower()
count = len(re.findall(r"sand|water|fish|sun", string))
print(count)

# string = input().lower()
# match = string.count("sand") + string.count("water") + string.count("fish") + string.count("sun")
# print(match)
