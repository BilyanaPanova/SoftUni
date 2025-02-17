def forecast(*args):
    dict_info = {"Sunny":[],"Cloudy":[],"Rainy":[]}
    for location,weather in args:
        dict_info[weather].append(location)
    result = ""
    for key,value in dict_info.items():
        for v in sorted(value):
            result += f"{v} - {key}\n"
    return result.strip()

print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))