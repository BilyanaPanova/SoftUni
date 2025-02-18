def summing_side(side):
    sum = 0
    for number in side:
        if number == 0:
            sum *= 0.8
        sum += number
    return sum


path_cars = [int(x) for x in input().split(" ")]
middle_index = len(path_cars) // 2
left_car = path_cars[:middle_index]
right_car = path_cars[-1:middle_index:-1]

if summing_side(left_car) < summing_side(right_car):
    print(f"The winner is left with total time: {summing_side(left_car):.1f}")
else:
    print(f"The winner is right with total time: {summing_side(right_car):.1f}")
