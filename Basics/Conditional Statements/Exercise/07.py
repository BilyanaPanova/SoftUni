budget = float(input())
count_video_card = int(input())
count_processor = int(input())
count_ram = int(input())

price_video_card = count_video_card * 250
price_processor = (price_video_card * 0.35) * count_processor
price_ram = (price_video_card * 0.1) * count_ram
all_cost = price_ram + price_processor + price_video_card

if count_video_card > count_processor:
    all_cost = all_cost * 0.85

money_left = abs(budget - all_cost)

if all_cost > budget:
    print(f"Not enough money! You need {money_left:.2f} leva more!")
else:
    print(f"You have {money_left:.2f} leva left!")
