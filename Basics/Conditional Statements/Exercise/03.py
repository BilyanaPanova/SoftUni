from math import floor

hours = int(input())
minutes = int(input())

new_time = (hours * 60) + minutes + 15
new_hours = floor(new_time // 60)
new_minutes = new_time % 60

if new_hours == 24:
    new_hours = 0
elif new_minutes == 60:
    new_minutes = 0

if new_minutes < 10:
    print(f"{new_hours}:0{new_minutes}")
else:
    print(f"{new_hours}:{new_minutes}")
