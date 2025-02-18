from collections import deque

players = deque(input().split(", "))

ROWS = 6
COLUMNS = 6

maze = [input().split() for _ in range(ROWS)]

coordinate = input()

while coordinate:
    player = players.popleft()

    if player:
        row, col = [int(x) for x in coordinate.strip("()").split(", ")]

        if maze[row][col] == "E":
            print(f"{player} found the Exit and wins the game!")
            break
        elif maze[row][col] == "T":
            winner = "".join([x for x in players if x])
            print(f"{player} is out of the game! The winner is {winner}.")
            break
        elif maze[row][col] == "W":
            players.append(False)
            print(f"{player} hits a wall and needs to rest.")

        players.append(player)
    else:
        players.rotate(-1)

    coordinate = input()
