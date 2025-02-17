budget = float(input())
price_for_kilo_flour = float(input())

price_for_pack_of_eggs = price_for_kilo_flour * 0.75
price_for_litter_milk = price_for_kilo_flour * 1.25
price_for_one_bread = price_for_litter_milk / 4 + price_for_pack_of_eggs + price_for_kilo_flour

colored_eggs = 0
made_breads = 0

while True:
    if price_for_one_bread > budget:
        break
    else:
        budget -= price_for_one_bread
        made_breads += 1
        colored_eggs += 3
        if made_breads % 3 == 0:
            colored_eggs -= made_breads - 2

print(f"You made {made_breads} loaves of "
      f"Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
