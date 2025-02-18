store = {}
while True:
    command = input()
    if command == "statistics":
        print("Products in stock:")
        [print(f"- {product}: {quantity}") for product, quantity in store.items()]
        print(f"Total Products: {len(store.keys())}")
        print(f'Total Quantity: {sum(store.values())}')
        break

    key_product, value_quantity = command.split(": ")
    if key_product in store:
        store[key_product] += int(value_quantity)
    else:
        store[key_product] = int(value_quantity)

