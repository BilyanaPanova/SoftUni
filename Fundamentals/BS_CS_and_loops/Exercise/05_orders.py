number_of_orders = int(input())

price = 0
total_price = 0

for _ in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_needed_per_day = int(input())
    if days in range(1, 32) and capsules_needed_per_day in range(1, 2001) and 0.01 <= price_per_capsule <= 100:
        price = price_per_capsule * (days * capsules_needed_per_day)
        print(f"The price for the coffee is: ${price:.2f}")
        total_price += price
    else:
        continue
print(f"Total: ${total_price:.2f}")
