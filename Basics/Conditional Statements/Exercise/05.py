budget_for_film = float(input())
count_actors = int(input())
price_clothes_for_one_actor = float(input())

price_decor = budget_for_film * 0.10
price_clothes = count_actors * price_clothes_for_one_actor

if count_actors > 150:
    price_clothes = price_clothes * 0.9

all_cost = price_decor + price_clothes
money_left = abs(budget_for_film - all_cost)

if budget_for_film >= all_cost:
    print("Action!")
    print(f"Wingard starts filming with {money_left:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {money_left:.2f} leva more.")

