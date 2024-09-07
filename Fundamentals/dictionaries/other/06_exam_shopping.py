shop = {}
command = input()

while command != "shopping time":
    act,product,quantity = command.split()

    if product not in shop:
        shop[product] = int(quantity)
    else:
        shop[product] += int(quantity)

    command = input()

another_command = input()

while another_command != "exam time":
    act,product,quantity = another_command.split()

    if product in shop and shop[product] > 0:
        shop[product] -= int(quantity)
    elif product in shop and shop[product] <=0:
        print(f"{product} out of stock")
    elif product not in shop:
        print(f"{product} doesn't exist")

    another_command = input()

for product,quantity in shop.items():
    if quantity <= 0:
        continue
    print(f"{product} -> {quantity}")
