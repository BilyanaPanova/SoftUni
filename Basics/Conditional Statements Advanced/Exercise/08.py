hour_exam = int(input())
minute_exam = int(input())
hour_arrival= int(input())
minute_arrival= int(input())

all_min_exam = (hour_exam * 60) + minute_exam
all_min_arrival = (hour_arrival * 60) + minute_arrival
diff_minutes = abs(all_min_arrival - all_min_exam)

if all_min_arrival > all_min_exam:
    print("Late")
    if diff_minutes < 60:
        minutes = diff_minutes % 60
        print(f"{minutes} minutes after the start")
    elif diff_minutes >= 60:
        hour = diff_minutes // 60
        minutes = diff_minutes % 60
        print(f"{hour}:{minutes:02d} hours after the start")

elif all_min_arrival == all_min_exam or diff_minutes <= 30:
    print("On time")
    if diff_minutes <= 30 and diff_minutes != 0:
        print(f"{diff_minutes} minutes before the start")

else:
    print("Early")
    if diff_minutes >= 60:
        hour = diff_minutes // 60
        minutes = diff_minutes % 60
        print(f"{hour}:{minutes:02d} hours before the start")
    else:
        print(f"{diff_minutes} minutes before the start")
