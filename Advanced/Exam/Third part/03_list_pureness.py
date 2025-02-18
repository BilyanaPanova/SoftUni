from collections import deque


def best_list_pureness(numbers: list, key: int):
    numbers = deque(numbers)
    total_sum = 0
    rotation = 0
    for i in range(key+1):
        sum_nums = sum([(x * y) for x, y in enumerate(numbers)])
        if sum_nums > total_sum:
            total_sum = sum_nums
            rotation = i
        numbers.rotate()
    return f"Best pureness {total_sum} after {rotation} rotations"


test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)