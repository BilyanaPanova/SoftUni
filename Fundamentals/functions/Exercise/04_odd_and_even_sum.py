def even_odd_sum(numbers):
    even_sum = 0
    odd_sum = 0
    for num in numbers:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num
    return even_sum, odd_sum


number = input()
numbers = [int(x) for x in (map(str, number))]
sum_of_even_digits, sum_of_odd_digits = even_odd_sum(numbers)
print(f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}")
