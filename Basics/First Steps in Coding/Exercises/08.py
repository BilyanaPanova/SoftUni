year_tax = int(input())

price_shoes = year_tax * 0.6
price_outfit = price_shoes * 0.8
price_ball = price_outfit / 4
price_accessories = price_ball / 5
total_cost = price_accessories + price_outfit + price_ball + price_shoes + year_tax

print(total_cost)
