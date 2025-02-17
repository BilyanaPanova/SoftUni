numbers = [int(x) for x in input().split(", ")]

positive_numbers = [x for x in numbers if x >= 0]
negative_numbers = [x for x in numbers if x < 0]
even_numbers = [x for x in numbers if x % 2 == 0]
odd_numbers = [x for x in numbers if x % 2 != 0]

print(f"Positive: {', '.join(map(str,positive_numbers))}")
print(f"Negative: {', '.join(map(str,negative_numbers))}")
print(f"Even: {', '.join(map(str,even_numbers))}")
print(f"Odd: {', '.join(map(str,odd_numbers))}")
