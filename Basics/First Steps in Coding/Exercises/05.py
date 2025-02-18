count_pen = int(input()) * 5.80
count_marker = int(input()) * 7.20
cleaning_detergent = int(input()) * 1.20
discount = int(input()) / 100

needed_money = (count_pen + count_marker + cleaning_detergent) * (1 - discount)

print(f'{needed_money:.2f}')
