number = int(input())

for _ in range(number):
    number_code = int(input())
    if number_code == 88:
        print("Hello")
    elif number_code == 86:
        print("How are you?")
    elif number_code < 88:
        print("GREAT!")
    elif number_code > 88:
        print("Bye.")
