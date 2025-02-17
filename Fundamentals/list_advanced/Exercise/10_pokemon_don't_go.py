sequence_of_integers = [int(x) for x in input().split()]
upgrade_number = 0
sum_all_capture_pokemons = 0

while len(sequence_of_integers) != 0:
    index = int(input())

    if index < 0:
        upgrade_number = sequence_of_integers.pop(0)
        sequence_of_integers.insert(0, sequence_of_integers[-1])
    if index >= len(sequence_of_integers):
        upgrade_number = sequence_of_integers.pop(-1)
        sequence_of_integers.append(sequence_of_integers[0])
    if index in range(len(sequence_of_integers)):
        upgrade_number = sequence_of_integers.pop(index)

    sequence_of_integers = [x + upgrade_number if x <= upgrade_number else x - upgrade_number for x in
                            sequence_of_integers]
    sum_all_capture_pokemons += upgrade_number

print(sum_all_capture_pokemons)
