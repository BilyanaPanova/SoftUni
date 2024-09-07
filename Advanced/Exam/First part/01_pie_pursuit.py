from collections import deque

contestants = deque(map(int, input().split()))
pies = deque(map(int, input().split()))

while contestants and pies:
    diff = contestants.popleft() - pies.pop()

    if diff > 0:
        contestants.append(diff)
    elif diff < 0:
        if diff == -1 and pies:
            pies[-1] += abs(diff)
        else:
            pies.append(abs(diff))

if not contestants and not pies:
    print("We have a champion!")
elif contestants:
    print("We will have to wait for more pies to be baked!")
    print(f"Contestants left: {', '.join(map(str, contestants))}")
elif pies:
    print("Our contestants need to rest!")
    print(f"Pies left: {', '.join(map(str, pies))}")


