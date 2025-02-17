def shop_from_grocery_list(budget:int,grocery_list:list,*args):
    products = []
    for name_product,price in args:
        if name_product in grocery_list and name_product not in products and price <= budget:
            grocery_list.remove(name_product)
            products.append(name_product)
            budget -= price
        elif price > budget:
            break
    if not grocery_list:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."
    else:
        return f"You did not buy all the products. Missing products: {', '.join(grocery_list)}."

