import math

towns = {}
input_line = input()
while input_line != "Aggregate":
    town,shell = input_line.split()
    if town not in towns:
        towns[town] = []
    if int(shell) not in towns[town]:
        towns[town].append(int(shell))
    input_line = input()
for key,value in towns.items():
    average_shells = sum(value) - (sum(value)/len(value))
    print(f"{key} -> {', '.join(map(str,value))} ({math.ceil(average_shells)})")
