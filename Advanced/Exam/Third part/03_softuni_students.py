def softuni_students(*args, **kwargs):
    courses = {}
    students = {}

    for course_id, username in args:
        students[username] = course_id

    for course_id, course_name in kwargs.items():
        courses[course_id] = course_name

    valid_students = []
    invalid_students = []

    for username, course_id in students.items():
        if course_id in courses:
            course_name = courses[course_id]
            valid_students.append([username, course_name])
        else:
            invalid_students.append(username)

    valid_students.sort(key=lambda x: x[0])

    result = ""
    for username, course_name in valid_students:
        result += f"*** A student with the username {username} has successfully finished the course {course_name}!\n"

    if invalid_students:
        result += f"!!! Invalid course students: {', '.join(sorted(invalid_students))}"

    return result.strip()

