def valid_check(contest_and_pass, contest_, password_):
    if contest_ in contest_and_pass.keys() and contest_and_pass[contest] == password_:
        return True
    return False


def add_contest_and_pass():
    dict_of_contests_and_passwords = {}
    while True:
        input_line = input()
        if input_line == "end of contests":
            break
        contest_, password_ = input_line.split(":")
        dict_of_contests_and_passwords[contest_] = password_
    return dict_of_contests_and_passwords


def sorting_dict(my_dict):
    for key, value in my_dict.items():
        my_dict[key] = dict(sorted(value.items(), key=lambda x: x[1], reverse=True))
    sorted_dict = dict(sorted(my_dict.items()))
    return sorted_dict


def best_candidate(my_dict):
    max_value = 0
    name = ""
    for key, value in my_dict.items():
        sum_value = sum(my_dict[key].values())
        if sum_value > max_value:
            max_value = sum_value
            name = key
    return max_value, name


def output(my_dict):
    total_points, user = best_candidate(my_dict)
    print(f"Best candidate is {user} with total {total_points} points.")
    print("Ranking:")
    for names, val_dict in my_dict.items():
        print(f"{names}")
        for key_contest, val_points in val_dict.items():
            print(f"#  {key_contest} -> {val_points}")


contest_and_passwords = add_contest_and_pass()
interview_info = {}
while True:
    info = input()

    if info == "end of submissions":
        interview_info = sorting_dict(interview_info)
        output(interview_info)
        break

    contest, password, username, points = info.split("=>")
    points = int(points)

    if valid_check(contest_and_passwords, contest, password):
        if username not in interview_info:
            interview_info[username] = {}
        elif contest in interview_info[username].keys():
            old_points = interview_info[username][contest]
            points = max(old_points, points)
        interview_info[username].update({contest: points})
