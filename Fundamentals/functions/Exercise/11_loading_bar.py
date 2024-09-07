def loading_bar(number):
    if number < 100:
        percent = number // 10
        dot = 10 - percent
        print(f"{number}% [{percent*'%'}{dot*'.'}]\nStill loading...")
    elif number == 100:
        print("100% Complete!\n[%%%%%%%%%%]")


number = int(input())
loading_bar(number)
