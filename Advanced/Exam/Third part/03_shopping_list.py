from functools import reduce


def shopping_list(budget: int, **kwargs):
    min_budget = 100
    if budget < min_budget:
        return "You do not have enough budget."

    total_product_price = {}
    for name_product, quantity_price in kwargs.items():
        total_product_price[name_product] = reduce(lambda x, y: x * y, quantity_price)

    bought_products = []
    limit = 5
    for name,total_price in total_product_price.items():
        if total_price <= budget:
            budget -= total_price
            bought_products.append(f"You bought {name} for {total_price:.2f} leva.")
        if len(bought_products) == limit:
            break
    return f"\n".join(bought_products)


print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))