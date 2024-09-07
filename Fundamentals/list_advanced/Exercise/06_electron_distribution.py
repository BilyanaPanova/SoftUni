number_of_electrons = int(input())

shells = []
starting_number = 1

while True:
    filling = 2 * (starting_number ** 2)

    if filling + sum(shells) < number_of_electrons:
        shells.append(filling)
    elif filling > number_of_electrons:
        shells.append(number_of_electrons - sum(shells))
        break

    starting_number += 1

print(shells)
