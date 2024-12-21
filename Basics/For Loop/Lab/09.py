number = int(input())

sum1 = 0
sum2 = 0

for i in range(1, number + 1):
    sum1 = sum1 + int(input())

for i in range(1, number + 1):
    sum2 = sum2 + int(input())

if sum1 == sum2:
    print(f"Yes, sum = {sum1}")
else:
    print(f"No, diff = {abs(sum1 - sum2)}")
