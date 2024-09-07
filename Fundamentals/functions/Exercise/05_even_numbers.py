def even_numb(x):
    if x % 2 == 0:
        return x


numbers = [int(x) for x in input().split(" ")]
even_numbers = list(filter(even_numb, numbers))
print(even_numbers)
