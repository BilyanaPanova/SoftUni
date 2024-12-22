count_tab = int(input())
salary = int(input())

left_money = salary
for i in range(1, count_tab + 1):
    web_page = input()
    if web_page == "Facebook":
        left_money -= 150
    elif web_page == "Instagram":
        left_money -= 100
    elif web_page == "Reddit":
        left_money -= 50
    else:
        continue

    if left_money == 0:
        print("You have lost your salary.")
        break

if left_money > 0:
    print(f"{left_money:.0f}")
