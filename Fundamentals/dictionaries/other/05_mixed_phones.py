dict_with_phone_numbers = {}
input_phone = input().split(" : ")

while input_phone[0] != "Over":

    if input_phone[0].isdigit():
        dict_with_phone_numbers[input_phone[1]] = input_phone[0]
    else:
        dict_with_phone_numbers[input_phone[0]] = input_phone[1]

    input_phone = input().split(" : ")

for name in sorted(dict_with_phone_numbers.keys()):
    print(f"{name} -> {dict_with_phone_numbers[name]}")
