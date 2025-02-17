import re

def tail_type(fish_tail):
    if len(fish_tail) > 5:
        return f"Long ({len(fish_tail)*2} cm)"
    elif len(fish_tail) > 1:
        return f"Medium ({len(fish_tail)*2} cm)"
    elif len(fish_tail) == 1:
        return "Short (2 cm)"
    else:
        return "None"


def body_type(fish_body):
    if len(fish_body) > 10:
        return f"Long ({len(fish_body)*2} cm)"
    elif len(fish_body) > 5:
        return f"Medium ({len(fish_body)*2} cm)"
    else:
        return f"Short ({len(fish_body)*2} cm)"


def head_type(fish_head):
    if fish_head == "'":
        return "Awake"
    elif fish_head == "-":
        return "Asleep"
    else:
        return "Dead"


pattern = r"((>+)?<(\(+)('|x|-)>)"
matches = re.findall(pattern, input())
if matches:
    for index, elements in enumerate(matches, start=1):
        fish = elements[0]
        tail = elements[1]
        body = elements[2]
        head = elements[3]

        print(f"Fish {index}: {fish}")
        print(f" Tail type: {tail_type(tail)}")
        print(f" Body type: {body_type(body)}")
        print(f" Status: {head_type(head)}")
else:
    print("No fish found.")
