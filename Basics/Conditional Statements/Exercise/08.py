from math import ceil

name_serial = input()
time_episode = int(input())
time_afternoon_rest = int(input())

lunch_time = time_afternoon_rest / 8
relax_time = time_afternoon_rest / 4
rest_of_time = time_afternoon_rest - lunch_time - relax_time
diff = ceil(abs(rest_of_time - time_episode))

if rest_of_time >= time_episode:
    print(f'You have enough time to watch {name_serial} and left with {diff} minutes free time.')
else:
    print(f"You don't have enough time to watch {name_serial}, you need {diff} more minutes.")
