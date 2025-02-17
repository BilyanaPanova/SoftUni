from math import floor
count_pages = int(input())
pages_for_one_hour = int(input())
count_days = int(input())

total_time_for_reading = count_pages / pages_for_one_hour
hours_day =floor(total_time_for_reading / count_days)

print(hours_day)
