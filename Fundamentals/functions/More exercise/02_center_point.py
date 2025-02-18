import math


first_coordinates = [float(input()), float(input())]
second_coordinates = [float(input()), float(input())]


if sum(abs(x) for x in first_coordinates) <= sum(abs(x) for x in second_coordinates):
    first_coordinates = tuple([math.floor(x) for x in first_coordinates])
    print(first_coordinates)
else:
    second_coordinates = tuple([math.floor(x) for x in second_coordinates])
    print(second_coordinates)
