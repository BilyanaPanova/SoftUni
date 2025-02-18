from collections import deque

time = deque([int(x) for x in input().split()])
tasks = [int(x) for x in input().split()]

duck_dict = {60: {"Darth Vader Ducky": 0}, 120: {"Thor Ducky": 0}, 180: {"Big Blue Rubber Ducky": 0},
             240: {"Small Yellow Rubber Ducky": 0}}

while time and tasks:
    curr_time = time.popleft()
    curr_task = tasks.pop()
    value = curr_time * curr_task
    for key in duck_dict.keys():
        if value <= key:
            duck_dict[key] = {k: v + 1 for k, v in duck_dict[key].items()}
            break
    else:
        tasks.append(curr_task - 2)
        time.append(curr_time)

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
dict_values = [list(*value.items()) for value in duck_dict.values()]
for key, value in dict_values:
    print(f"{key}: {value}")
