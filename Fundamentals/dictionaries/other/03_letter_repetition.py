import collections

some_string = input()

dict_with_letters = dict(collections.Counter(some_string))

for key,val in dict_with_letters.items():
    print(f"{key} -> {val}")
