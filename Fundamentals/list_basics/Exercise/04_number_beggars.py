numbers = [int(x) for x in input().split(", ")]
beggars = int(input())
list_with_sum = []

for beggar in range(beggars):
    part_for_beggar = sum(numbers[beggar::beggars])
    list_with_sum.append(part_for_beggar)

print(list_with_sum)
