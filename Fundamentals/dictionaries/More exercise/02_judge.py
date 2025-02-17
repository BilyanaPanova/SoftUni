def sorting_dictionary(my_dict):
    sorted_dict = dict(sorted(my_dict.items(), key=lambda x: len(x)))
    for key, value in sorted_dict.items():
        sorted_dict[key] = dict(sorted(value.items(), key=lambda x: (-x[1], x[0])))
    return sorted_dict


def first_output(my_dict):
    my_dict = sorting_dictionary(my_dict)
    dict_for_second_print = {}
    for contest_name, value_dict in my_dict.items():
        print(f"{contest_name}: {len(my_dict[contest_name].values())} participants")
        enumerate_number = 0
        for name, point in value_dict.items():
            enumerate_number += 1
            print(f"{enumerate_number}. {name} <::> {point}")
            if name not in dict_for_second_print:
                dict_for_second_print[name] = 0
            dict_for_second_print[name] += point
    return dict_for_second_print


def second_output(my_dict):
    my_dict = first_output(my_dict)
    sorted_dict = dict(sorted(my_dict.items()))
    sorted_dict = dict(sorted(sorted_dict.items(), key=lambda x: x[1],reverse=True))

    print(f"Individual standings:")
    enumerate_number = 0
    for name, total_points in sorted_dict.items():
        enumerate_number += 1
        print(f"{enumerate_number}. {name} -> {total_points}")


judge_system = {}
while True:
    input_line = input()
    if input_line == "no more time":
        second_output(judge_system)
        break

    username, contest, points = input_line.split(" -> ")
    points = int(points)

    if contest not in judge_system:
        judge_system[contest] = {}
    elif username in judge_system[contest].keys():
        old_points = judge_system[contest][username]
        points = max(old_points, points)
    judge_system[contest].update({username: points})
