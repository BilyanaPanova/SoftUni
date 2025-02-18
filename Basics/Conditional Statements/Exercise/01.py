from math import floor

first_time = int(input())
second_time = int(input())
third_time = int(input())

all_time = first_time + second_time + third_time
minutes = floor(all_time // 60)
seconds = all_time % 60

if seconds < 10:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")
