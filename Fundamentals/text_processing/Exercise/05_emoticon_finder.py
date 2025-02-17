text = input()

for index, symbol in enumerate(text):

    if symbol == ":":
        print(symbol + text[index+1])
