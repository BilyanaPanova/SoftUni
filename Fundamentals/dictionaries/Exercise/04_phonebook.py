def output(my_dict_of_phonenumbers, search_name):
    if search_name in my_dict_of_phonenumbers:
        print(f"{search_name} -> {my_dict_of_phonenumbers[search_name]}")
    else:
        print(f"Contact {search_name} does not exist.")


def input_names(number_of_names):
    for _ in range(number_of_names):
        searched_name = input()
        output(phonebook, searched_name)


phonebook = {}

while True:
    input_line = input()

    if input_line.isdigit():
        count_of_names = int(input_line)
        input_names(count_of_names)
        break

    name, phone = input_line.split("-")
    phonebook[name] = phone
