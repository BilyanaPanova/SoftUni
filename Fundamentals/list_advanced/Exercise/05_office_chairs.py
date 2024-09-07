number_of_rooms = int(input())
free_chairs = 0
flag = True

for room in range(1, number_of_rooms + 1):
    chairs, visitor = input().split()
    chairs = len(chairs)
    visitor = int(visitor)

    if chairs < visitor:
        needed_chairs = visitor - chairs
        print(f"{needed_chairs} more chairs needed in room {room}")
        flag = False
    else:
        free_chairs += chairs - visitor

if flag:
    print(f"Game On, {free_chairs} free chairs left")
