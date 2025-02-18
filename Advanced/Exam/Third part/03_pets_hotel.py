def accommodate_new_pets(capacity:int,max_w:float,*animals):
    accommodated_pets = {}
    result = ""
    for pet,weight in animals:
        if sum(accommodated_pets.values()) == capacity:
            result += "You did not manage to accommodate all pets!\n"
            break
        if max_w >= weight:
            if pet not in accommodated_pets:
                accommodated_pets[pet] = 0
            accommodated_pets[pet] += 1
    else:
        result += f"All pets are accommodated! Available capacity: {capacity - sum(accommodated_pets.values())}.\n"
    result += "Accommodated pets:\n"
    for key in sorted(accommodated_pets.keys()):
        result += f"{key}: {accommodated_pets[key]}\n"

    return result.strip()

print(accommodate_new_pets(
    2,
    15.0,
    ("dog", 10.0),
    ("cat", 5.8),
    ("cat", 2.7),
))