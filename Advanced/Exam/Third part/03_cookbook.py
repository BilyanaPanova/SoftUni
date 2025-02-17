def cookbook(*args):
    cook_dict = {}
    for name, cuisine, list_ in args:
        if cuisine not in cook_dict:
            cook_dict[cuisine] = {}
        cook_dict[cuisine][name] = list_
    cook_dict = dict(sorted(cook_dict.items(), key=lambda x: (-len(x[1]), x[0])))
    result = ""
    for key, value in cook_dict.items():
        result += f"{key} cuisine contains {len(value)} recipes:\n"
        value = dict(sorted(value.items()))
        for k, v in value.items():
            result += f"  * {k} -> Ingredients: {', '.join(v)}\n"
    return result.strip()


print(cookbook(
    ("Pad Thai", "Thai", ["rice noodles", "shrimp", "peanuts", "bean sprouts", "tamarind sauce"])
    ))