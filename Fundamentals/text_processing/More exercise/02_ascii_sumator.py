first_symbol = input()
second_symbol = input()
string = input()
total = 0

for symbol in string:
    if ord(symbol) in range(ord(first_symbol)+1, ord(second_symbol)):
        total += ord(symbol)

print(total)
