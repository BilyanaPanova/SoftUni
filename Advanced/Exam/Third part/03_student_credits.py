def students_credits(*some_strings):
    dict_info = {}
    for curr_string in some_strings:
        course_name, credits_, test_points, d_points = curr_string.split("-")
        if course_name not in dict_info:
            dict_info[course_name] = 0
        add_credits = (int(d_points) / int(test_points)) * int(credits_)
        dict_info[course_name] += add_credits

    result = ""
    total_credits = sum(dict_info.values())
    if total_credits < 240:
        diff = 240 - total_credits
        result += f"Diyan needs {diff:.1f} credits more for a diploma.\n"
    else:
        result += f"Diyan gets a diploma with {total_credits:.1f} credits.\n"

    dict_info = sorted(dict_info.items(), key=lambda x: -x[1])
    for course, points in dict_info:
        result += f"{course} - {points:.1f}\n"

    return result.strip()
