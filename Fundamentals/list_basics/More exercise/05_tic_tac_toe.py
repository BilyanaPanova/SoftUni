playground = []

for _ in range(3):
    playground.append(input().split(" "))

first_player = []
second_player = []

for el in playground:
    for index, symbol in enumerate(el):
        if "1" == symbol:
            first_player.append(index)
        if "2" == symbol:
            second_player.append(index)

first_player = "".join(map(str, first_player))
second_player = "".join(map(str, second_player))

if first_player == "012" or \
        first_player == "210" or \
        first_player == "000" or \
        first_player == "111" or \
        first_player == "222":
    print("First player won")
elif second_player == "012" or \
        second_player == "210" or \
        second_player == "000" or \
        second_player == "111" or \
        second_player == "222":
    print("Second player won")
else:
    print("Draw!")

#
# first_row = input().split()
# second_row = input().split()
# third_row = input().split()
#
# name_player = "First"
# found = False
#
# for player in range(1, 3):
#     player = str(player)
#     line = [player, player, player]
#     if line == first_row or second_row == line or third_row == line:  # преверка на редовете
#         found = True
#     for index in range(0, 3):
#         if first_row[index] == player and second_row[index] == player and third_row[index] == player:  # проверка на колоните
#             found = True
#     if first_row[0] == player and second_row[1] == player and third_row[2] == player:  # ляв диагонал
#         found = True
#     elif first_row[2] == player and second_row[1] == player and third_row[0] == player:  # десен диагонал
#         found = True
#     if found:
#         print(f"{name_player} player won")
#         break
#     name_player = "Second"
# else:
#     print("Draw!")
