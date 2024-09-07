string = input().split(" ")
shuffle = int(input())
half_index = int(len(string) / 2)

for _ in range(shuffle):
    left_side = string[:half_index]
    right_side = string[half_index:]
    string.clear()

    for index in range(len(left_side)):
        string.append(left_side[index])
        string.append(right_side[index])

print(string)
