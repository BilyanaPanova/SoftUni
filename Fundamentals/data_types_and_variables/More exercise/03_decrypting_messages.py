key = int(input())
input_lines = int(input())

message = ""

for _ in range(input_lines):
    letter = input()
    message += chr(ord(letter) + key)

print(message)
