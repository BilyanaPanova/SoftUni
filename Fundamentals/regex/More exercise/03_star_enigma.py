import re

number_of_messages = int(input())
planet_information = {"Attacked planets": [], "Destroyed planets": []}

for _ in range(number_of_messages):
    encrypted_message = input()
    decrypt_kode = sum([1 if x in ("s", "t", "a", "r") else 0 for x in encrypted_message.lower()])
    decrypted_message = "".join([chr(ord(x) - decrypt_kode) for x in encrypted_message])
    pattern = (r"@(?P<planet_name>[a-zA-Z]+)[^\@\-\!\:\>]*"
               r":(?P<planet_population>\d+)[^\@\-\!\:\>]*"
               r"!(?P<attack_type>[AD])![^\@\-\!\:\>]*"
               r"->(?P<soldier_count>\d+)")
    match = re.search(pattern, decrypted_message)
    if match:
        if match['attack_type'] == "A":
            planet_information["Attacked planets"].append(match["planet_name"])
        else:
            planet_information["Destroyed planets"].append(match["planet_name"])

for key, value in planet_information.items():
    print(f"{key}: {len(value)}")
    for planets in sorted(value):
        print(f"-> {planets}")
