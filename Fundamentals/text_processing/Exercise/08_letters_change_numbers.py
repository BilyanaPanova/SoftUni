import re
import string

sequence_of_strings = input().split()

dict_with_alphabet_values = {letter: value for value, letter in enumerate(string.ascii_lowercase, start=1)}
total_value = 0

for string in sequence_of_strings:

    start_letter, end_letter = re.findall(r"\D", string)
    number = int(*(re.findall(r"\d+", string)))
    total = number

    if start_letter.isupper():
        total /= dict_with_alphabet_values[start_letter.lower()]
    elif start_letter.islower():
        total *= dict_with_alphabet_values[start_letter]

    if end_letter.isupper():
        total -= dict_with_alphabet_values[end_letter.lower()]
    elif end_letter.islower():
        total += dict_with_alphabet_values[end_letter]

    total_value += total

print(f"{total_value:.2f}")
