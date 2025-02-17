day_stay = int(input())
room = input()
rating = input()

night_stay = day_stay - 1
price_all_night_stay = 0

if room == "room for one person":
    price_all_night_stay = night_stay * 18.00
  
elif room == "apartment":
    price_all_night_stay = night_stay * 25.00
    if day_stay < 10:
        price_all_night_stay = price_all_night_stay * 0.70
    elif 10 <= day_stay <= 15:
        price_all_night_stay = price_all_night_stay * 0.65
    elif day_stay > 15:
        price_all_night_stay = price_all_night_stay * 0.50
      
elif room == "president apartment":
    price_all_night_stay = night_stay * 35.00
    if day_stay < 10:
        price_all_night_stay = price_all_night_stay * 0.90
    elif 10 <= day_stay <= 15:
        price_all_night_stay = price_all_night_stay * 0.85
    elif day_stay > 15:
        price_all_night_stay = price_all_night_stay * 0.80

if rating == "positive":
    price_all_night_stay = price_all_night_stay * 1.25
elif rating == "negative":
    price_all_night_stay = price_all_night_stay * 0.90

print(f"{price_all_night_stay:.2f}")

