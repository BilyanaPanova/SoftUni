dict_with_ages = {}
dict_with_salary = {}
dict_with_position = {}

while True:
    command = input()
    if command == "filter base":
        break
    name,information = command.split(" -> ")
    if "." in information:
        dict_with_salary[name] = float(information)
    elif information.isalpha():
        dict_with_position[name] = information
    else:
        dict_with_ages[name] = int(information)
input_line = input()

if input_line == "Age":
    for name,ages in dict_with_ages.items():
        print(f"Name: {name}")
        print(f"Age: {ages}")
        print("====================")
elif input_line == "Salary":
    for name,salary in dict_with_salary.items():
        print(f"Name: {name}")
        print(f"Salary: {salary}")
        print("====================")
else:
    for name,position in dict_with_position.items():
        print(f"Name: {name}")
        print(f"Position: {position}")
        print("====================")
