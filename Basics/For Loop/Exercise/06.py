actor = input()
points_from_academy = float(input())
count_jury = int(input())

jury_points = 0
all_points = 0
for i in range(1, count_jury + 1):
    name_jury = input()
    points_from_jury = float(input())
    jury_points += (len(name_jury) * points_from_jury) / 2
    all_points = points_from_academy + jury_points
    if all_points >= 1250.5:
        break
if all_points >= 1250.5:
    print(f"Congratulations, {actor} got a nominee for leading role with {all_points:.1f}!")
else:
    print(f"Sorry, {actor} you need {(1250.5 - all_points):.1f} more!")
