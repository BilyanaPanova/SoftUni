def shopping_cart(*all_products):
    products = {"Dessert": [], "Soup": [], "Pizza": []}

    for tuple_p in all_products:

        if tuple_p == "Stop":
            break

        type_of_meal, product = tuple_p

        try:
            if product not in products[type_of_meal]:
                products[type_of_meal].append(product)
        except AttributeError:
            continue

        for i, v in enumerate(products.values(), start=2):
            if i == len(v) and isinstance(v, list):
                products[type_of_meal] = tuple(v)

    if all(not v for v in products.values()):
        return "No products in the cart!"

    products = dict(sorted(products.items(), key=lambda x: (-len(x[1]), x[0])))
    result = ""

    for key, value in products.items():
        result += f"{key}:\n"

        for p in sorted(value):
            result += f" - {p}\n"

    return result.strip()


print(shopping_cart('Stop', ('Pizza', 'ham'), ('Pizza', 'mushrooms'), ))
