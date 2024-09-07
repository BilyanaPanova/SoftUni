import itertools

input_line = int(input())

brackets = []

for _ in range(input_line):
    line = input()

    if line == "(" or line == ")":
        brackets.append(line)

brackets = [x + y for x, y in itertools.zip_longest(brackets[::2], brackets[1::2], fillvalue="1")]

if len(set(brackets)) == 1 and brackets[0] == "()":
    print("BALANCED")
else:
    print("UNBALANCED")



# Решение на Иван Шопов

# input_line = int(input())
# some_string = ""
# for _ in range(input_line):
#     line = input()
#
#     if line == "(" or line == ")":
#         some_string += line
#
# some_string = some_string.replace("()", "")
#
# if not some_string:
#     print("BALANCED")
# else:
#     print("UNBALANCED")
