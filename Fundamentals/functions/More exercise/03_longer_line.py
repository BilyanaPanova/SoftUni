import math


def sorted_line(line):
    line = sorted(line, key=lambda x: abs(x[0]) + abs(x[1]))
    return line[0], line[1]


first_line = [float(input()), float(input()), float(input()), float(input())]
second_line = [float(input()), float(input()), float(input()), float(input())]

if sum([abs(x) for x in first_line]) >= sum([abs(x) for x in second_line]):
    first_line_line = [(math.floor(x), math.floor(y)) for x, y in zip(first_line[::2], first_line[1::2])]
    el1, el2 = sorted_line(first_line_line)
    print(f"{el1}{el2}")
else:
    second_line = [(math.floor(x), math.floor(y)) for x, y in zip(second_line[::2], second_line[1::2])]
    el1, el2 = sorted_line(second_line)
    print(f"{el1}{el2}")
