population = [int(x) for x in input().split(", ")]
minimum_wealth = int(input())

for index,people in enumerate(population):
    max_num = max(population)
    index_max_num = population.index(max_num)
    if people < minimum_wealth:
        diff = minimum_wealth - people
        max_num -= diff
        population[index_max_num] = max_num
        people += diff
        population[index] = people

if sum(population) >= minimum_wealth * len(population):
    print(population)
else:
    print("No equal distribution possible")
