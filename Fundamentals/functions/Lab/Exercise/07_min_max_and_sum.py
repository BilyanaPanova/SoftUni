def min_max_sum(sequence):
    min_num = min(sequence)
    max_num = max(sequence)
    sum_nums = sum(sequence)
    return min_num, max_num, sum_nums


numbers = [int(x) for x in input().split(" ")]
min_value, max_value, sum_numbers = min_max_sum(numbers)

print(f"The minimum number is {min_value}")
print(f"The maximum number is {max_value}")
print(f"The sum number is: {sum_numbers}")
