working_day_events = input().split("|")
energy = 100
coins = 100
for current_even in working_day_events:
    even, number = current_even.split("-")
    if even == "rest":
        current_energy = 0
        if energy + int(number) > 100:
            current_energy = 100 - energy
            energy = 100
        else:
            energy += int(number)
            current_energy = int(number)
        print(f"You gained {current_energy} energy.")
        print(f"Current energy: {energy}.")
    elif even == "order":
        if energy - 30 < 0:
            print("You had to rest!")
            energy += 50
        else:
            energy -= 30
            coins += int(number)
            print(f"You earned {number} coins.")
    else:
        if coins - int(number) < 0:
            print(f"Closed! Cannot afford {even}.")
            break
        else:
            print(f"You bought {even}.")
            coins -= int(number)
else:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
