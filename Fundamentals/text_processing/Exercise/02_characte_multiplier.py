from itertools import zip_longest


def total_sum(zipped_string):
    total = 0
    for el in zipped_string:
        total += el[0] * el[1]
    return total


first_word, second_word = input().split()
first_word = [ord(x) for x in first_word]
second_word = [ord(x) for x in second_word]
zipped_ord_elements = list(zip_longest(first_word, second_word, fillvalue=1))

print(total_sum(zipped_ord_elements))
