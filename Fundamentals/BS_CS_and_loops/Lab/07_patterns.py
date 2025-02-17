number = int(input())

for col in range(1, number + 1):
    for row in range(col):
        print("*", end="")
    print()

for col in range(number - 1, 0, -1):
    for row in range(col):
        print("*", end="")
    print()
