searched_string = input().split(", ")
sequences = input()
find_elements = []
for el in searched_string:
    if el in sequences and el not in find_elements:
        find_elements.append(el)
print(find_elements)
