lessons_and_exercise = input().split(", ")
while True:
    input_line = input()

    if input_line == "course start":
        pass

    input_line = input_line.split(":")
    command = input_line[0]
    lesson_title = input_line[1]
    if command == "Add":
        lessons_and_exercise.append(lesson_title)

    elif command == "Insert":
        index = int(input_line[2])
        if lesson_title not in lessons_and_exercise:
            lessons_and_exercise.insert(index, lesson_title)

    elif command == "Remove":
        if lesson_title in lessons_and_exercise:
            lessons_and_exercise.remove(lesson_title)

    elif command == "Swap":
        second_lesson_title = input_line[2]
        if lesson_title in lessons_and_exercise and second_lesson_title in lessons_and_exercise:
            first_lesson_index = lessons_and_exercise.index(lesson_title)
            second_lesson_index = lessons_and_exercise.index(second_lesson_title)
            lessons_and_exercise[first_lesson_index],lessons_and_exercise[second_lesson_index] = (
                lessons_and_exercise[second_lesson_index],lessons_and_exercise[first_lesson_index])

    elif command == "Exercise":
        pass