dict_of_products = {}
while True:
    input_line = input()

    if input_line == "buy":

        for name_product, dict_items in dict_of_products.items():
            total_price = dict_items[0] * dict_items[1]
            print(f"{name_product} -> {total_price:.2f}")

        break

    name, price, quantity = input_line.split()
    price = float(price)
    quantity = int(quantity)

    if name not in dict_of_products:
        dict_of_products[name] = [price, quantity]
    else:
        list_of_elements = dict_of_products.get(name)
        quantity += list_of_elements[1]
        dict_of_products[name] = [price, quantity]
