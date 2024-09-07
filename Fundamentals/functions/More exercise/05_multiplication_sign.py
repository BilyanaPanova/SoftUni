def negative_sign(numbers):
    count_of_negative_sign = 0
    for number in numbers:
        if "-" in number:
            count_of_negative_sign += 1
        if number == "0":
            return "zero"
    if count_of_negative_sign % 2 != 0:
        return "negative"
    return "positive"


numbers = [input(),input(),input()]
print(negative_sign(numbers))
