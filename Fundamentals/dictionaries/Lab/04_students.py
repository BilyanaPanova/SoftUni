dict_of_courses = {}
while True:
    command = input()
    if ":" in command:
        name, id_student, course = command.split(":")
        if course not in dict_of_courses:
            dict_of_courses[course] = name + " - " + id_student
        else:
            dict_of_courses[course] += "\n" + name + " - " + id_student

    else:
        name_of_the_course = command.replace("_", " ")
        print(dict_of_courses.setdefault(name_of_the_course))
        break
