from collections import deque

tools = deque([int(x) for x in input().split()])
substances = [int(x) for x in input().split()]
challenges = [int(x) for x in input().split()]

while tools and substances:
    tool = tools.popleft()
    substance = substances.pop()
    value = tool * substance

    if value in challenges:
        challenges.remove(value)
        if not challenges:
            print("Harry found an ostracon, which is dated to the 6th century BCE.")
            break
        continue

    tools.append(tool + 1)
    substance -= 1

    if substance:
        substances.append(substance)
else:
    print("Harry is lost in the temple. Oblivion awaits him.")

if tools:
    print(f"Tools: {', '.join(map(str,tools))}")
if substances:
    print(f"Substances: {', '.join(map(str,substances))}")
if challenges:
    print(f"Challenges: {', '.join(map(str,challenges))}")
