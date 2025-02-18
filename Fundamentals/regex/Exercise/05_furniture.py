import re

bought_furniture = []
total_money = 0
while True:
    input_line = input()

    if input_line == "Purchase":
        print("Bought furniture:")
        for furniture in bought_furniture:
            print(furniture)
        print(f"Total money spend: {total_money:.2f}")
        break

    pattern = r">>(?P<Furniture>\b[A-Z]+)<<(?P<Price>[0-9]+\.?[0-9]+)!(?P<Count>[0-9]+)"
    matches = re.finditer(pattern, input_line, re.IGNORECASE)

    for match in matches:
        dict_match = match.groupdict()
        bought_furniture.append(dict_match["Furniture"])
        total_money += float(dict_match["Price"]) * int(dict_match["Count"])




