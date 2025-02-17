courses = {}
while True:
    input_line = input()

    if input_line == "end":
        for course, list_of_students in courses.items():
            print(f"{course}: {len(list_of_students)}")
            print(f"-- " + "\n-- ".join(list_of_students))
        break

    course_name, student_name = input_line.split(" : ")

    if course_name not in courses:
        courses[course_name] = []

    courses[course_name].append(student_name)
