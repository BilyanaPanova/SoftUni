age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

total_money = 0
toy = 0
money = 0
money_for_brother = 0

for num in range(1, age + 1):
    if num % 2 == 0:
        money_for_brother += 1
        money += 10
        for i in range(10, money + 1, 10):
           total_money += 10
    else:
        toy += 1

sum_money = total_money - money_for_brother
sum_toy = toy * toy_price
total = sum_money + sum_toy

if washing_machine_price > total:
    print(f"No! {(washing_machine_price - total):.2f}")
elif washing_machine_price <= total:
    print(f"Yes! {(total - washing_machine_price):.2f}")
