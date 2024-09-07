numbers = [int(x) for x in input().split(" ")]
count_number_to_remove = int(input())

sorted_numbers = sorted(numbers)
removed_numbers = sorted_numbers[:count_number_to_remove]
numbers = [str(x) for x in numbers if x not in removed_numbers]

print(", ".join(numbers))
