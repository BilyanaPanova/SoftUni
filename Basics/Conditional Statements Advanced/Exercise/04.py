budget = int(input())
season = input()
count_fishman = int(input())

price_ship = 0
discount = 0

if season == "Spring":
    price_ship = 3000

    if count_fishman <= 6:
        discount += 0.1
    elif 7 <= count_fishman <= 11:
        discount += 0.15
    elif count_fishman >= 12:
        discount += 0.25

elif season == "Summer":
    price_ship = 4200

    if count_fishman <= 6:
        discount += 0.1
    elif 7 <= count_fishman <= 11:
        discount += 0.15
    elif count_fishman >= 12:
        discount += 0.25

elif season == "Autumn":
    price_ship = 4200

    if count_fishman <= 6:
        discount += 0.1
    elif 7 <= count_fishman <= 11:
        discount += 0.15
    elif count_fishman >= 12:
        discount += 0.25

elif season == "Winter":
    price_ship = 2600

    if count_fishman <= 6:
        discount += 0.1
    elif 7 <= count_fishman <= 11:
        discount += 0.15
    elif count_fishman >= 12:
        discount += 0.25

total = price_ship - (price_ship * discount)

if season != "Autumn" and count_fishman % 2 == 0:
    total = total * 0.95

left_money = abs(budget - total)

if budget >= total:
    print(f"Yes! You have {left_money:.2f} leva left.")
else:
    print(f"Not enough money! You need {left_money:.2f} leva.")
