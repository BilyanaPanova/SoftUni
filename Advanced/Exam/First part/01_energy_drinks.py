from collections import deque

milligrams_of_caffeine = [int(x) for x in input().split(", ")]
energy_drinks = deque(int(x) for x in input().split(", "))

curr_caffeine = 0
MAX_CAFFEINE = 300
DEGREASE_CAFFEINE = 30

while milligrams_of_caffeine and energy_drinks:
    first_n = milligrams_of_caffeine.pop()
    second_n = energy_drinks.popleft()

    curr_value = first_n * second_n

    if curr_value + curr_caffeine <= MAX_CAFFEINE:
        curr_caffeine += curr_value
    else:
        energy_drinks.append(second_n)
        curr_caffeine = max(curr_caffeine-30, 0)

if energy_drinks:
    print(f'Drinks left: {", ".join(map(str,energy_drinks))}')
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {curr_caffeine} mg caffeine.")
