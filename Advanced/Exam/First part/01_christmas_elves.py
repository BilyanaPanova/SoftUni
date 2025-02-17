from collections import deque


def find_valid_elf(energy_p):
    while energy_p:
        if energy[0] >= MIN_NEED_ENERGY:
            return energy.popleft()
        energy.popleft()
    return


def success_operation(box, diff, dict_info, energy_p):
    dict_info["made toys"] += 1
    dict_info["used energy"] += box
    energy_p.append(diff + 1)
    return dict_info, energy_p


def third_count(box, diff, dict_info, energy_p):
    diff -= box
    if diff >= 0:
        dict_info["made toys"] += 2
        dict_info["used energy"] += box * 2
        energy_p.append(diff + 1)
    else:
        return dict_info, no_energy(energy_p, box)

    if counter % 5 == 0:
        dict_info["made toys"] -= 2
        energy_p[-1] -= 1

    return dict_info, energy_p


def fifth_count(box, diff, dict_info, energy_p):
    dict_info["used energy"] += box
    energy_p.append(diff)
    return dict_info, energy_p


def no_energy(energy_p, box):
    global boxes
    global curr_elf
    energy_p.append(curr_elf * 2)
    boxes.append(box)
    return energy_p


MIN_NEED_ENERGY = 5
energy = deque(int(x) for x in input().split())
boxes = [int(x) for x in input().split()]
counter = 0
info = {"made toys": 0, "used energy": 0}
while energy and boxes:
    curr_elf = find_valid_elf(energy)
    curr_box = boxes.pop()
    counter += 1
    try:
        curr_diff = curr_elf - curr_box
    except TypeError:
        boxes.append(curr_box)
        break
    if curr_diff >= 0:
        if counter % 3 == 0:
            info, energy = third_count(curr_box, curr_diff, info, energy)
        elif counter % 5 == 0:
            info, energy = fifth_count(curr_box, curr_diff, info, energy)
        else:
            info, energy = success_operation(curr_box, curr_diff, info, energy)
    else:
        energy = no_energy(energy, curr_box)

print(f"Toys: {info['made toys']}")
print(f"Energy: {info['used energy']}")
if energy:
    print(f"Elves left: {', '.join(map(str, energy))}")
if boxes:
    print(f"Boxes left: {', '.join(map(str, boxes))}")
