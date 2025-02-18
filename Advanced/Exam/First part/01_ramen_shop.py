from collections import deque

bowls = [int(x) for x in input().split(", ")]
customers = deque(int(x) for x in input().split(", "))

while bowls and customers:
    curr_bowl = bowls.pop()
    curr_customer = customers.popleft()

    diff = curr_bowl - curr_customer
    if diff != 0:
        bowls.append(diff) if diff > 0 else customers.appendleft(abs(diff))

print("Great job! You served all the customers.") if not customers else print(
    "Out of ramen! You didn't manage to serve all customers.")

if bowls:
    print(f"Bowls of ramen left: {', '.join(map(str, bowls))}")
if customers:
    print(f"Customers left: {', '.join(map(str, customers))}")
