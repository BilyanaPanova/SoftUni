number = float(input())


def definer(numb):
    result = ""
    if numb == 0:
        result = "zero"
    elif 0 < abs(numb) < 1:
        result = "small "
    elif abs(numb) > 1000000:
        result = "large "

    if numb > 0:
        result += "positive"
    elif numb < 0:
        result += "negative"
    return result


print(definer(number))
