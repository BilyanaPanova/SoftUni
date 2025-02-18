numbers = [[int(y) for y in x] for x in input().split(" ")]
string = input()
message = ""

for number in numbers:
    index = sum(number)
    if index >= len(string):
        index %= len(string)
    message += string[index]
    string = string[:index] + string[index+1:]

print(message)
