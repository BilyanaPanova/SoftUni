def data_type_function(x, y):
    if x == "int":
        return eval(y) * 2
    elif x == "real":
        return f"{(eval(y) * 1.5):.2f}"
    else:
        return f"$" + y + "$"


data_type = input()
number = input()
print(data_type_function(data_type, number))
