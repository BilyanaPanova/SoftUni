dwarf_info = {}
while True:
    input_line = input()

    if input_line == "Once upon a time":
        dwarfs = dict(sorted(dwarf_info.items(), key=lambda x: (-x[1], x[0])))
        for key, value in dwarfs.items():
            hat_color, name = key.split(" ")
            print(f"({hat_color}) {name} <-> {value}")
        break

    name, hat_color, physics = input_line.split(" <:> ")
    name_and_hat_color = hat_color + " " + name
    physics = int(physics)
    if name_and_hat_color in dwarf_info.keys():
        old_points = dwarf_info[name_and_hat_color]
        physics = max(old_points, physics)
    dwarf_info[name_and_hat_color] = physics




import collections


def search_name(dwarfs_, name_):
    for keys, values in dwarfs_.items():
        if name_ == dwarfs[keys]["name"]:
            return True
    return False


def search_color(dwarfs_, color_):
    for keys, values in dwarfs_.items():
        if color_ == dwarfs_[keys]["color"]:
            return True
    return False


def search_max_physic(dwarfs_, name_, color_, physic_):
    for keys, values in dwarfs_.items():
        if name_ in values.values() and color_ in values.values():
            old_points = dwarfs_[keys]["physic"]
            dwarfs_[keys]["physic"] = max(old_points, physic_)
    return dwarfs_


def keyfunc(tup):
    key, d = tup
    d1 = d["physic"]
    d2 = collections.Counter(d["color"])
    return -d1,d2


dwarfs = {}
number_dwarfs = 1
while True:
    input_line = input()
    if input_line == "Once upon a time":
        sorted_d = dict(sorted(dwarfs.items(),key= lambda x: keyfunc(x)))
        print(sorted_d)
        # dwarfs = dict(sorted(dwarfs.items(), key=lambda x: (x[1]["physic"],collections.Counter(x[1]["color"]))))
        # for key, value in dwarfs.items():
        #     hat_color = dwarfs[key]["color"]
        #     name = dwarfs[key]["name"]
        #     physics = dwarfs[key]["physic"]
        #     print(f"({hat_color}) {name} <-> {physics}")
        break

    dwarf_name, dwarf_hat_color, dwarf_physics = input_line.split(" <:> ")
    if not search_name(dwarfs, dwarf_name) or not search_color(dwarfs, dwarf_hat_color):
        dwarfs[number_dwarfs] = {"name": dwarf_name, "color": dwarf_hat_color, "physic": int(dwarf_physics)}
        number_dwarfs += 1
    elif search_name(dwarfs, dwarf_name) and search_color(dwarfs, dwarf_hat_color):
        dwarfs = search_max_physic(dwarfs, dwarf_name, dwarf_hat_color, int(dwarf_physics))
