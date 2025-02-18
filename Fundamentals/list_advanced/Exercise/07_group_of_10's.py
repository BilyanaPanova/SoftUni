sequence_of_numbers = [int(x) for x in input().split(", ")]
group = 10

while len(sequence_of_numbers) > 0:
    list_of_numbers = [x for x in sequence_of_numbers if x <= group]
    print(f"Group of {group}'s: {list_of_numbers}")
    group += 10
    sequence_of_numbers = [x for x in sequence_of_numbers if x not in list_of_numbers]
    