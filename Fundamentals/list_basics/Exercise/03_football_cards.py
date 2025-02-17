team_A = [x for x in range(1, 12)]
team_B = team_A.copy()
sequence_of_cards = input().split(" ")
flag = True

for card in sequence_of_cards:
    team,number_player = card.split("-")

    if team == "A" and int(number_player) in team_A:
        team_A.remove(int(number_player))
    elif team == "B" and int(number_player) in team_B:
        team_B.remove(int(number_player))

    if (len(team_A) or len(team_B)) < 7:
        flag = False
        break

print(f"Team A - {len(team_A)}; Team B - {len(team_B)}")
if not flag:
    print("Game was terminated")
