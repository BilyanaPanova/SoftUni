wardrobe = {}
number_of_lines = int(input())

for _ in range(number_of_lines):
    color, clothes = input().split(" -> ")

    if color not in wardrobe:
        wardrobe[color] = {}

    for clothing_item in clothes.split(","):

        if clothing_item not in wardrobe[color].keys():
            wardrobe[color][clothing_item] = 0

        wardrobe[color][clothing_item] += 1
search_color, *searched_item = input().split()

for color, items in wardrobe.items():
    print(f"{color} clothes:")

    for item, count in items.items():

        if search_color == color and searched_item[0] == item:
            print(f"* {item} - {count} (found!)")
        else:
            print(f"* {item} - {count}")
