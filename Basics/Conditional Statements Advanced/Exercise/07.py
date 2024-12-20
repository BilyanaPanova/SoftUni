month = input()
count_night = int(input())

price_studio = 0
price_apartment = 0
price_of_entire_stay_in_studio = 0
price_of_entire_stay_in_apartment = 0

if month == "May" or month == "October":
    price_studio = 50
    price_apartment = 65
    if 7 < count_night < 14:
        price_studio = price_studio * 0.95
    elif count_night > 14:
        price_studio = price_studio * 0.70
        price_apartment = price_apartment * 0.9


elif month == "June" or month == "September":
    price_studio = 75.2
    price_apartment = 68.70
    if count_night > 14:
        price_studio = price_studio * 0.80
        price_apartment = price_apartment * 0.9

elif month == "July" or month == "August":
    price_studio = 76
    price_apartment = 77
    if count_night > 14:
        price_apartment = price_apartment * 0.9

price_of_entire_stay_in_studio = count_night * price_studio
price_of_entire_stay_in_apartment = count_night * price_apartment

print(f"Apartment: {price_of_entire_stay_in_apartment:.2f} lv.")
print(f"Studio: {price_of_entire_stay_in_studio:.2f} lv.")
