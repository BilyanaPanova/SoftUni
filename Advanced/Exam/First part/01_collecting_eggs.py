from collections import deque

eggs = deque(int(x) for x in input().split(", "))
papers = deque(int(x) for x in input().split(", "))

total_count = 0
BOX_SIZE = 50
while eggs and papers:
    egg = eggs.popleft()

    if egg <= 0:
        continue
    if egg == 13:
        papers[0], papers[-1] = papers[-1], papers[0]
        continue

    paper = papers.pop()
    curr_sum = egg + paper
    if curr_sum <= BOX_SIZE:
        total_count += 1

print(f"Great! You filled {total_count} boxes.") if total_count else print("Sorry! You couldn't fill any boxes!")
if eggs:
    print(f'Eggs left: {", ".join(map(str, eggs))}')
if papers:
    print(f'Pieces of paper left: {", ".join(map(str, papers))}')
