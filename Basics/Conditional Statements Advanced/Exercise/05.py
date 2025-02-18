budget = float(input())
season = input()

destination = ''
place = ''
money_spend = 0

if budget <= 100:
    destination = "Bulgaria"
  
    if season == "summer":
        money_spend = budget * 0.3
        place = "Camp"
    elif season == "winter":
        money_spend = budget * 0.7
        place = "Hotel"
      
elif budget <= 1000:
    destination = "Balkans"
  
    if season == "summer":
        money_spend = budget * 0.4
        place = "Camp"
    elif season == "winter":
        money_spend = budget * 0.8
        place = "Hotel"
      
elif budget > 1000:
    destination = "Europe"
    place = "Hotel"
    money_spend = budget * 0.9

print(f"Somewhere in {destination}")
print(f"{place} - {money_spend:.2f}")
