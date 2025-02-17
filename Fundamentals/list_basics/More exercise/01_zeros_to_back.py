numbers = [int(x) for x in input().split(", ")]
zeros = numbers.count(0)
numbers = [x for x in numbers if x != 0] + [0] * zeros
print(numbers)
