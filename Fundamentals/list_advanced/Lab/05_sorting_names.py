names = input().split(", ")
names.sort()
names = sorted(names, key=lambda x: len(x), reverse=True)
print(names)
