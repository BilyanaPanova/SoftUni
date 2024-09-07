def is_perfect(number):
    sum_divisors = 0
    for num in range(1, number):
        if number % num == 0:
            sum_divisors += num
    if sum_divisors == number:
        return True
    return False


number = int(input())
if is_perfect(number):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")
