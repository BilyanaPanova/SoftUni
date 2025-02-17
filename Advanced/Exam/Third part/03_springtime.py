def start_spring(**kwargs):
    dict_el = {}
    for k, v in kwargs.items():
        if v not in dict_el.keys():
            dict_el[v] = []
        dict_el[v].append(k)
    sorted_elements = dict(sorted(dict_el.items(), key=lambda x: (-len(x[1]), x[0])))
    result = []
    for key, value in sorted_elements.items():
        result.append(f"{key}:\n")
        for el in sorted(value):
            result.append(f"-{el}\n")
    return "".join(result)

example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))