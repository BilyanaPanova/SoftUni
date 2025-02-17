def is_in_range(item, price):
    flag = True
    if item == "Clothes" and price <= 50:
        pass
    elif item == "Shoes" and price <= 35:
        pass
    elif item == "Accessories" and price <= 20.50:
        pass
    else:
        flag = False
    return flag


items_with_prices = [x.split("->") for x in input().split("|")]
budget = float(input())
ticket = 150
bought_items = []

for el in items_with_prices:
    item = el[0]
    price = float(el[1])
    if is_in_range(item, price) and price <= budget:
        budget -= price
        bought_items.append(price)

sold_items = [x * 1.40 for x in bought_items]
profit = sum(sold_items) - sum(bought_items)
total = sum(sold_items) + budget
sold_items = ["%.2f" % x for x in sold_items]
print(*sold_items)
print(f"Profit: {profit:.2f}")
if total >= ticket:
    print("Hello, France!")
else:
    print("Not enough money.")
