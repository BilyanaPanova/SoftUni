def tribonacci_sequence(number):
    sequence = [1]
    for _ in range(1, number):
        sum_of_last_tree_numbers = sum(sequence[-3:])
        sequence.append(sum_of_last_tree_numbers)
    print(*sequence)


count_of_numbers = int(input())
tribonacci_sequence(count_of_numbers)
