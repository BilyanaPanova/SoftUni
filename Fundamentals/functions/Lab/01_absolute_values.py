numbers = [float(x) for x in input().split(" ")]


def absolute_values(number):
    absolute_numbers = []
    for num in number:
        absolute_numbers.append(abs(num))
    return absolute_numbers


print(absolute_values(numbers))
