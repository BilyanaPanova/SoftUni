projections = input()
rows = int(input())
columns = int(input())

all_place = rows * columns
price = 0

if projections == "Premiere":
    price = 12
elif projections == "Normal":
    price = 7.50
elif projections == "Discount":
    price = 5
  
total_cost = all_place * price

print(f"{total_cost:.2f} leva")
