input_line = int(input())
number_list = []

for _ in range(input_line):
    number = int(input())
    number_list.append(number)

command = input()

if command == "even":
    number_list = [x for x in number_list if x % 2 == 0]
elif command == "odd":
    number_list = [x for x in number_list if x % 2 != 0]
elif command == "negative":
    number_list = [x for x in number_list if x < 0]
elif command == "positive":
    number_list = [x for x in number_list if x >= 0]

print(number_list)