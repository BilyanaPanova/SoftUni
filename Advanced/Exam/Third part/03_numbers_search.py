def numbers_searching(*args):
    sorted_numbers = sorted(args)
    numbers = [x for x in range(sorted_numbers[0], sorted_numbers[-1] + 1)]
    set_numbers = set(args)
    result = []
    result.append(*set(numbers) - set_numbers)
    result.append(sorted(set([item for item in args if args.count(item) > 1])))
    return result


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
