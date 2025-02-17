from collections import deque

pizzas = deque(int(x) for x in input().split(", "))
employees = [int(x) for x in input().split(", ")]

made_pizzas = 0

while pizzas and employees:
    curr_pizza = pizzas[0]
    curr_employer = employees[-1]

    if curr_pizza > 10:
        pizzas.popleft()
        continue

    if curr_pizza <= 0:
        pizzas.popleft()
        continue

    if curr_employer <= 0:
        employees.pop()
        continue

    if curr_pizza <= curr_employer:
        made_pizzas += curr_pizza
        pizzas.popleft()
        employees.pop()
    else:
        made_pizzas += employees[-1]
        pizzas[0] -= employees.pop()

if pizzas:
    print(f"Not all orders are completed.\nOrders left: {', '.join(map(str,pizzas))}")
else:
    print(f"All orders are successfully completed!\nTotal pizzas made: {made_pizzas}\n"
          f"Employees: {', '.join(map(str,employees))}")
