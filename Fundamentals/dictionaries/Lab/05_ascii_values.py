list_letters = input().split(", ")
list_ascii_values = [ord(x) for x in list_letters]
dict_letter_values = dict(zip(list_letters, list_ascii_values))
print(dict_letter_values)