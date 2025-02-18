import sys
num = int(input())

total = 0
max_number = -sys.maxsize

for i in range(1, num + 1):
    number = int(input())
    if number > max_number:
        max_number = number
    total += number

if max_number == total - max_number:
    print("Yes")
    print(f"Sum = {max_number}")
else:
    print("No")
    print(f"Diff = {abs(max_number - (total - max_number))}")
