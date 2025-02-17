import re


def letters_and_digit(some_sting):
    name_ = "".join(re.findall(r"[A-Za-z]+", some_sting))
    distance_ = sum([int(x) for x in re.findall(r"\d", some_sting)])
    return name_, distance_


participants = input().split(", ")
input_line = input()
value = 0
participants_information = dict.fromkeys(participants, value)

while input_line != "end of race":
    name, distance = letters_and_digit(input_line)

    if name in participants_information:
        participants_information[name] += distance

    input_line = input()

participants_information = sorted(participants_information.items(), key=lambda x: x[1], reverse=True)

print(f"1st place: {participants_information[0][0]}")
print(f"2nd place: {participants_information[1][0]}")
print(f"3rd place: {participants_information[2][0]}")

