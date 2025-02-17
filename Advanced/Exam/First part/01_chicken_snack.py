from collections import deque

money = [int(x) for x in input().split()]
food = deque([int(x) for x in input().split()])
food_count = 0

while money and food:
    value = money.pop() - food.popleft()

    if value >= 0:
        food_count += 1
        if money:
            money[-1] += value

if food_count >= 4:
    print(f"Gluttony of the day! Henry ate {food_count} foods.")
elif food_count == 0:
    print("Henry remained hungry. He will try next weekend again.")
elif food_count == 1:
    print(f"Henry ate: {food_count} food.")
else:
    print(f"Henry ate: {food_count} foods.")
