def sorting_cheeses(**kwargs):
    sorted_cheese = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))
    result = []
    for (cheese_name, quantities) in sorted_cheese:
        result.append(cheese_name)
        quantities = sorted(quantities, reverse=True)
        result += quantities
    return "\n".join(map(str, result))


print(sorting_cheeses(Parmesan=[102, 120, 135], Camembert=[100, 100, 105, 500, 430], Mozzarella=[50, 125], ))

print(sorting_cheeses(Parmigiano=[165, 215], Feta=[150, 515], Brie=[150, 125]))
