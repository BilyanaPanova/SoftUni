list_of_float_numbers = [float(x) for x in input().split()]
dict_with_numbers = {}

for number in list_of_float_numbers:

    if number not in dict_with_numbers.keys():
        dict_with_numbers[number] = 0

    dict_with_numbers[number] += 1

for key in sorted(dict_with_numbers.keys()):
    print(f"{key} -> {dict_with_numbers[key]} times")
