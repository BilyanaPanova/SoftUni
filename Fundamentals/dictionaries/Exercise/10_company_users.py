dict_of_company_info = {}

while True:
    input_line = input()

    if input_line == "End":

        for name, list_of_id in dict_of_company_info.items():
            print(f"{name}")
            print(f"-- " + "\n-- ".join(list_of_id))

        break

    company_name, ID = input_line.split(" -> ")

    if company_name not in dict_of_company_info:
        dict_of_company_info[company_name] = []

    if ID not in dict_of_company_info[company_name]:
        dict_of_company_info[company_name].append(ID)
