from collections import deque

customers = deque([int(x) for x in input().split(", ")])
taxis = [int(x) for x in input().split(", ")]

total_time = 0
while customers and taxis:
    curr_customer = customers.popleft()
    curr_taxi = taxis.pop()

    if curr_taxi >= curr_customer:
        total_time += curr_customer
    else:
        customers.appendleft(curr_customer)

if customers:
    print(f"Not all customers were driven to their destinations\nCustomers left: {', '.join(map(str,customers))}")
else:
    print(f"All customers were driven to their destinations\nTotal time: {total_time} minutes")
