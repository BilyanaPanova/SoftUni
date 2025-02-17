from functools import reduce


def operate(symbol, *numbers):
    if symbol == "+":
        return reduce(lambda x, y: x + y, numbers)
    elif symbol == "-":
        return reduce(lambda x, y: x - y, numbers)
    elif symbol == "*":
        return reduce(lambda x, y: x * y, numbers)
    elif symbol == "/":
        return reduce(lambda x, y: x / y, numbers)


print(operate("/", 10, 0, 3))
print(operate("*", 3, 4))
