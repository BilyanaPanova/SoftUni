country_names = input().split(", ")
capitals_cities = input().split(", ")

dict_of_country_and_capitals = {key: value for key, value in zip(country_names, capitals_cities)}

for country,city in dict_of_country_and_capitals.items():
    print(f"{country} -> {city}")
    