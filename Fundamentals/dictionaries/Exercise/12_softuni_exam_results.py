def add_information(dict_exam, key_name, points_number):
    if key_name in dict_exam:
        old_points = dict_exam[key_name]
        points_number = max(old_points, points_number)
    dict_exam[key_name] = points_number


def add_submissions(subm_dict, key_language):
    if key_language not in subm_dict:
        subm_dict[key_language] = 0
    subm_dict[key_language] += 1


def output(first_dict, second_dict):
    print("Results:")
    for names, result in first_dict.items():
        print(f"{names} | {result}")
    print("Submissions:")
    for lang, value in second_dict.items():
        print(f"{lang} - {value}")


exam_info = {}
submissions = {}
while True:
    command = input()

    if command == "exam finished":
        output(exam_info, submissions)
        break

    if "banned" in command:
        name, *ban = command.split("-")
        del exam_info[name]
        continue

    name, language, points = command.split("-")
    points = int(points)
    add_information(exam_info, name, points)
    add_submissions(submissions, language)
