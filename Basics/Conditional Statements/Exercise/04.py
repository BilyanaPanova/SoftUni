price_excursion = float(input())
count_puzzles = int(input())
count_doll = int(input())
count_teddy_bears = int(input())
count_minion = int(input())
count_truck = int(input())

order = count_truck + count_minion + count_doll + count_puzzles + count_teddy_bears
price = (count_truck * 2.00) + (count_minion * 8.20) \
    + (count_doll * 3.00) + (count_teddy_bears * 4.10) + (count_puzzles * 2.60)

if order >= 50:
    price = price * 0.75

rent = price * 0.10
total = price - rent
money_left = abs(price_excursion - total)

if price_excursion <= total:
    print(f"Yes! {money_left:.2f} lv left.")
else:
    print(f"Not enough money! {money_left:.2f} lv needed.")
