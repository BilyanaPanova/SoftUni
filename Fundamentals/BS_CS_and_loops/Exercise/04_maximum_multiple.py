divisor_number = int(input())
number_range = int(input())

largest_number = 0
for number in range(1, number_range + 1):
    if number % divisor_number == 0:
        largest_number = number
print(largest_number)
