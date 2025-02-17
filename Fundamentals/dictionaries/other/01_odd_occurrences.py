my_dict = {}
input_line = input().split()

for word in input_line:
    word = word.lower()

    if word not in my_dict:
        my_dict[word] = 0

    my_dict[word] += 1

valid_keys = [key for key,value in my_dict.items() if value % 2 != 0]
print(*valid_keys,sep=", ")
