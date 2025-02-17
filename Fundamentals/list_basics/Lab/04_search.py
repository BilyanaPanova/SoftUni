input_line = int(input())
word = input()
all_strings = []

for _ in range(input_line):
    string = input()
    all_strings.append(string)

filtered_list = [x for x in all_strings if word in x]
print(all_strings)
print(filtered_list)
