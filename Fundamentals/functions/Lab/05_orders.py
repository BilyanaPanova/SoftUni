def summing_orders(product,count):
    total_cost = 0
    if product == "coffee":
        total_cost = count * 1.50
    elif product == "water":
        total_cost = count * 1
    elif product == "coke":
        total_cost = count * 1.4
    elif product == "snacks":
        total_cost = count * 2
    return f"{total_cost:.2f}"


product = input()
count = int(input())
print(summing_orders(product,count))
