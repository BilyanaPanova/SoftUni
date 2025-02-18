count_nylon = int(input())
count_paint = int(input())
count_thinner = int(input())
count_hours = int(input())

nylon_cost = (count_nylon + 2) * 1.50
paint_cost = (count_paint * 1.1) * 14.50
thinner_cost = count_thinner * 5
all_cost = nylon_cost + paint_cost + thinner_cost + 0.40
money_for_worker_per_hour = all_cost * 0.30
total_money_for_worker = money_for_worker_per_hour * count_hours
total_sum = all_cost + total_money_for_worker

print(total_sum)
