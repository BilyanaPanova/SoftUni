def equal_position(my_dict, p1, p2):
    for key, value in my_dict[p1].items():
        if key in my_dict[p2].keys():
            return key


def update_information(my_dict, player_, position_, skill_):
    if player_ not in my_dict:
        my_dict[player_] = {}
    elif position_ in my_dict[player_].keys():
        old_skill = my_dict[player_][position_]
        skill_ = max(old_skill, skill_)
    my_dict[player_].update({position_: skill_})
    return my_dict


def duel(my_dict, player_one, player_two):
    if player_one in my_dict and player_two in my_dict:
        if equal_position(my_dict, player_one, player_two):
            same_skill = equal_position(my_dict, player_one, player_two)
            if my_dict[player_one][same_skill] > my_dict[player_two][same_skill]:
                del my_dict[player_two]
            elif my_dict[player_one][same_skill] < my_dict[player_two][same_skill]:
                del my_dict[player_one]
    return my_dict


def sorted_information(my_dict):
    sorted_dict = dict(sorted(my_dict.items(), key=lambda x: (-sum(x[1].values()), x[0])))
    for key, value in sorted_dict.items():
        sorted_dict[key] = dict(sorted(value.items(), key=lambda x: (-x[1], x[0])))
    return sorted_dict


def output(my_dict):
    my_dict = sorted_information(my_dict)
    for name, values in my_dict.items():
        total_skills = sum(values.values())
        print(f"{name}: {total_skills} skill")
        for position_, skill_ in values.items():
            print(f"- {position_} <::> {skill_}")


players_information = {}
while True:
    command = input()

    if command == "Season end":
        output(players_information)
        break

    elif "->" in command:
        player, position, skill = command.split(" -> ")
        skill = int(skill)
        players_information = update_information(players_information, player, position, skill)

    elif "vs" in command:
        player1, player2 = command.split(" vs ")
        players_information = duel(players_information, player1, player2)
