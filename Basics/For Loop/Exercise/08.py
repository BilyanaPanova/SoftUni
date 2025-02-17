number_tournaments = int(input())
starting_points = int(input())

points_earned = 0
wins = 0


for tournament in range(number_tournaments):
    position = input()

    if position == 'W':
        points_earned += 2000
        wins += 1

    elif position == 'F':
        points_earned += 1200

    elif position == 'SF':
        points_earned += 720

total_point = starting_points + points_earned
print(f"Final points: {total_point}")
print(f"Average points: {points_earned // number_tournaments}")
print(f"{(wins / number_tournaments * 100):.2f}%")
