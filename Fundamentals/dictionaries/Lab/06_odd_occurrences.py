import collections

sequences = [x.lower() for x in input().split()]
dict_sequences = collections.Counter(sequences)
for key, value in dict_sequences.items():
    if value % 2 != 0:
        print(key, end=" ")

