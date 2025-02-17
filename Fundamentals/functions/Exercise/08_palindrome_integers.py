def is_palindrome(number):
    list_number = list(number)
    reverse_number = list_number[::-1]
    if list_number == reverse_number:
        return True
    return False


numbers = [int(x) for x in input().split(", ")]
for numb in numbers:
    str_number = str(numb)
    if is_palindrome(str_number):
        print("True")
    else:
        print("False")
