from collections import deque


def output(fs, rotation=10):
    print(f"Seat matches: {', '.join(fs)}")
    print(f"Rotations count: {rotation}")


seats = input().split(", ")
f_numbers = deque(int(x) for x in input().split(", "))
s_numbers = deque(int(x) for x in input().split(", "))

found_seats = []
for r in range(1, 11):
    first_number = f_numbers.popleft()
    second_number = s_numbers.pop()
    letter = chr(first_number + second_number)
    variations = (str(first_number) + letter, str(second_number) + letter)

    for v in variations:
        if v in seats:
            found_seats.append(v)
            seats.remove(v)
            break
    else:
        f_numbers.append(first_number)
        s_numbers.appendleft(second_number)

    if len(found_seats) == 3:
        output(found_seats, r)
        break
else:
    output(found_seats)
