number_of_snowballs = int(input())
snowball_value = 0
max_weight = 0
max_time = 0
max_quality = 0

for _ in range(number_of_snowballs):
    weight = int(input())
    time = int(input())
    quality = int(input())
    calculate = (weight / time) ** quality
    
    if calculate > snowball_value:
        snowball_value = calculate
        max_time = time
        max_quality = quality
        max_weight = weight

print(f"{max_weight} : {max_time} = {int(snowball_value)} ({max_quality})")
