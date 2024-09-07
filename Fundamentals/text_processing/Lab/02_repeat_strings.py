sequence_of_strings = input().split()
repeat_strings = [x*len(x) for x in sequence_of_strings]
print("".join(repeat_strings))
