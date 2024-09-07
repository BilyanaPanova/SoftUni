list_events = ['coding', 'dog', 'cat', 'movie']
coffees = 0

enter = input()
while enter != "END":
    if enter in map(str.upper, list_events):
    # if enter in [x.upper() for x in list_events]:
        coffees += 2
    elif enter in list_events:
        coffees += 1
    enter = input()
else:
    if coffees > 5:
        print("You need extra sleep")
    else:
        print(coffees)
