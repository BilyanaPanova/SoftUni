student_grades_dict = {}

number_of_loots = int(input())
for _ in range(number_of_loots):
    student_name = input()
    grade = float(input())

    if student_name not in student_grades_dict:
        student_grades_dict[student_name] = []

    student_grades_dict[student_name].append(grade)

for name, list_of_grades in student_grades_dict.items():
    average_grade = sum(list_of_grades) / len(list_of_grades)

    if average_grade >= 4.50:
        print(f"{name} -> {average_grade:.2f}")
