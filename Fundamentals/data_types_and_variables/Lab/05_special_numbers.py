number_range = int(input())
special_sum = [5, 7, 11]

for number in range(1, number_range + 1):
    if sum([int(x) for x in str(number)]) in special_sum:
        print(f"{number} -> True")
    else:
        print(f"{number} -> False")
