numbers = [int(x) for x in input().split(", ")]
index_even_number_list = []

for index, element in enumerate(numbers):
    if element % 2 == 0:
        index_even_number_list.append(index)

print(index_even_number_list)