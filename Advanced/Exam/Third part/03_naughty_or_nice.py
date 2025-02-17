def naughty_or_nice_list(list_names: list, *args, **kwargs):
    names_dict = {"Nice": [], "Naughty": [], "Not found": []}

    for command in args:
        number, key = command.split("-")
        number = int(number)
        match = [el for el in list_names if el[0] == number]
        if len(match) == 1:
            names_dict[key].append(match[0][1])
            list_names.remove(*match)

    for name, key in kwargs.items():
        match = [el for el in list_names if el[1] == name]

        if len(match) == 1:
            names_dict[key].append(match[0][1])
            list_names.remove(*match)

    for el in list_names:
        names_dict["Not found"].append(el[1])

    result = ""
    for key,names in names_dict.items():
        if names:
            result += f"{key}: {', '.join(names)}\n"

    return result


print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))
