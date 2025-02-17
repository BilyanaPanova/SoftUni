from math import pi
shape = input()

if shape == "square":
    length = float(input())
    area = length * length
    print(f"{area:.3f}")
elif shape == "rectangle":
    length = float(input())
    width = float(input())
    area = length * width
    print(f"{area:.3f}")
elif shape == "circle":
    radius = float(input())
    area = radius * radius * pi
    print(f"{area:.3f}")
elif shape == "triangle":
    length = float(input())
    height = float(input())
    area = length * height / 2
    print(f"{area:.3f}")
