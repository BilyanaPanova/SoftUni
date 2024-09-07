employees_happiness = [int(x) for x in input().split()]
factor = int(input())

multiply_happiness_with_factor = list(map(lambda x: x * factor, employees_happiness))
average = sum(multiply_happiness_with_factor) / len(employees_happiness)
happy_employees = [x for x in multiply_happiness_with_factor if x >= average]

if len(happy_employees) >= (len(employees_happiness) / 2):
    print(f"Score: {len(happy_employees)}/{len(employees_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(happy_employees)}/{len(employees_happiness)}. Employees are not happy!")
