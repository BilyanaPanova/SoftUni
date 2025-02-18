number = int(input())


def check_prime(number):
    for num in range(2, number):
        if number % num == 0:
            return False
    return True


print(check_prime(number))
