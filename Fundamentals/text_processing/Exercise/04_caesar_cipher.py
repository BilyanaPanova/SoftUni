text = input()

encrypt_version = [chr(ord(x)+3) for x in text]

print("".join(encrypt_version))
