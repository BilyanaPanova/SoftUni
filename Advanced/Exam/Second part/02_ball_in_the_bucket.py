def win_prize(points):
    prizes = {300: "Lego Construction Set", 200: "Teddy Bear", 100: "Football"}
    for key in prizes.keys():
        if points >= key:
            return f"Good job! You scored {points} points, and you've won {prizes[key]}."
    return f"Sorry! You need {100 - points} points more to win a prize."


matrix = [input().split() for _ in range(6)]

total_result = 0

for _ in range(3):
    curr_r, curr_c = [int(x) for x in input().strip("()").split(", ")]

    if curr_r in range(6) and curr_c in range(6):
        if matrix[curr_r][curr_c] == "B":
            total_result += sum([int(row[curr_c]) for row in matrix if row[curr_c].isdigit()])
            matrix[curr_r][curr_c] = "0"

print(win_prize(total_result))
