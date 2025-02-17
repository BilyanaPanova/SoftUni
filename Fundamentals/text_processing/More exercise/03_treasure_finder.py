import itertools

key_sequence = [int(x) for x in input().split()]

while True:
    message_to_decrypt = input()

    if message_to_decrypt == "find":
        break

    decrypted_message = [chr(ord(x) - y) for x, y in zip(message_to_decrypt, itertools.cycle(key_sequence))]
    decrypted_message = "".join(decrypted_message)
    material = decrypted_message[decrypted_message.index("&")+1:
                                 decrypted_message.index("&", decrypted_message.index("&")+1)]
    coordinates = decrypted_message[decrypted_message.index("<")+1:decrypted_message.index(">")]

    print(f"Found {material} at {coordinates}")
