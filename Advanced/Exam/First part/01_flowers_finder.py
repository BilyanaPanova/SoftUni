from collections import deque


def check_letters(fl, sl, flowers):
    for flower in flowers.keys():
        if fl in flowers[flower]:
            flowers[flower] = flowers[flower].replace(fl, "")
        if sl in flower:
            flowers[flower] = flowers[flower].replace(sl, "")
    return flowers


def find_flowers(flowers):
    for key, value in flowers.items():
        if not value:
            return key
    return None


vowels = deque(input().split())
consonants = input().split()

searched_flowers = {"rose": "rose", "tulip": "tulip", "lotus": "lotus", "daffodil": "daffodil"}

while vowels and consonants:
    first_letter = vowels.popleft()
    second_letter = consonants.pop()
    searched_flowers = check_letters(first_letter, second_letter, searched_flowers)
    got_flower = find_flowers(searched_flowers)
    if got_flower:
        print(f"Word found: {got_flower}")
        break
else:
    print("Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")
