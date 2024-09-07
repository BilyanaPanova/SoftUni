def sum_numbers(a, b):
    return a + b


def subtract(x, y):
    return x - y


def add_and_subtract(a, b, c):
    return subtract(sum_numbers(n1, n2), n3)


n1 = int(input())
n2 = int(input())
n3 = int(input())
print(add_and_subtract(n1, n2, n3))
