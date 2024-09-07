from collections import deque


def list_manipulator(numbers:list, command:str, part:str, *args):
    numbers = deque(numbers)
    if command == "add":
        if part == "beginning":
            numbers.extendleft(args[::-1])
        elif part == "end":
            numbers.extend(args)

    elif command == "remove":
        if part == "beginning":
            if args:
                n = args[0]
                for _ in range(n):
                    numbers.popleft()
            else:
                numbers.popleft()
        elif part == "end":
            if args:
                n = args[0]
                for _ in range(n):
                    numbers.pop()
            else:
                numbers.pop()
    numbers = list(numbers)
    return numbers


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
