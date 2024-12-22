count_groups = int(input())

musala = 0
monblan = 0
kilimandjaro = 0
k2 = 0
everest = 0
count = 0
for i in range(1, count_groups + 1):
    people_in_group = int(input())
    count += people_in_group
    if people_in_group <= 5:
        musala += people_in_group
    elif 6 <= people_in_group <= 12:
        monblan += people_in_group
    elif 13 <= people_in_group <= 25:
        kilimandjaro += people_in_group
    elif 26 <= people_in_group <= 40:
        k2 += people_in_group
    elif people_in_group >= 41:
        everest += people_in_group

print(f"{(musala / count * 100):.2f}%")
print(f"{(monblan / count * 100):.2f}%")
print(f"{(kilimandjaro / count * 100):.2f}%")
print(f"{(k2 / count * 100):.2f}%")
print(f"{(everest / count * 100):.2f}%")
