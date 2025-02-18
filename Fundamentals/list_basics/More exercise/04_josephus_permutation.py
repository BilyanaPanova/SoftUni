people_in_the_circle = input().split()
count = int(input())
killed_people = []

while len(people_in_the_circle) != 0:
    index = count - 1

    if len(people_in_the_circle) <= index:
        index = index % (len(people_in_the_circle))

    executed_person = people_in_the_circle.pop(index)
    killed_people.append(executed_person)
    people_in_the_circle = people_in_the_circle[index:] + people_in_the_circle[:index]

result = ",".join(killed_people)
print(f"[{result}]")


#2
# from collections import deque
#
# people = deque(input().split())
# number = int(input())
# killed_people = []
# while people:
#     people.rotate(-number+1)
#     killed_people.append(people.popleft())
#
# result = ",".join(killed_people)
# print(f"[{result}]")