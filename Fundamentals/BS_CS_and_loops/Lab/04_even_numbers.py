numbers = int(input())
flag = True

for _ in range(numbers):
    number = int(input())

    if number % 2 != 0:
        flag = False
        print(f"{number} is odd!")
        break

if flag:
    print("All numbers are even.")
