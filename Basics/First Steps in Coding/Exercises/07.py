count_chicken_menu = int(input())
count_fish_menu = int(input())
count_vegetarian_menu = int(input())

price_chicken_menu = count_chicken_menu * 10.35
price_fish_menu = count_fish_menu * 12.40
price_vegetarian_menu = count_vegetarian_menu * 8.15
all_cost = price_vegetarian_menu + price_chicken_menu + price_fish_menu
price_desert = all_cost * 0.20
total = all_cost + price_desert + 2.50

print(total)
