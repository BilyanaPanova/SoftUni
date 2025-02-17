def gather_credits(needed_credits: int, *args):
    dict_info = {}

    for name, points in args:
        if sum(dict_info.values()) >= needed_credits:
            break
        if name not in dict_info:
            dict_info[name] = points

    if sum(dict_info.values()) >= needed_credits:
        return (f"Enrollment finished! Maximum credits: {sum(dict_info.values())}."
                f"\nCourses: {', '.join(sorted(dict_info.keys()))}")
    return (f"You need to enroll in more courses! "
            f"You have to gather {needed_credits-sum(dict_info.values())} credits more.")


print(gather_credits(
    0))

