flower = input()
count_flower = int(input())
budget = int(input())

price = 0
all_cost = 0

if flower == "Roses":
    price = 5
  
    if count_flower > 80:
        all_cost = (count_flower * price) * 0.9
    else:
        all_cost = count_flower * price
      
elif flower == "Dahlias":
    price = 3.80
  
    if count_flower > 90:
        all_cost = (count_flower * price) * 0.85
    else:
        all_cost = count_flower * price
      
elif flower == "Tulips":
    price = 2.80
  
    if count_flower > 80:
        all_cost = (count_flower * price) * 0.85
    else:
        all_cost = count_flower * price
      
elif flower == "Narcissus":
    price = 3
  
    if count_flower < 120:
        all_cost = (count_flower * price) * 1.15
    else:
        all_cost = count_flower * price
      
elif flower == "Gladiolus":
    price = 2.50
  
    if count_flower < 80:
        all_cost = (count_flower * price) * 1.20
    else:
        all_cost = count_flower * price

left_money = abs(budget - all_cost)

if budget >= all_cost:
    print(f"Hey, you have a great garden with {count_flower} "
          f"{flower} and {left_money:.2f} leva left.")
else:
    print(f"Not enough money, you need {left_money:.2f} leva more.")
