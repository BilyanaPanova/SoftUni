notes = input()
to_do_list = []

while notes != "End":
    notes = notes.split("-")
    to_do_list.append(notes)
    notes = input()

to_do_list = sorted(to_do_list, key=lambda x: int(x[0]))
to_do_list = [x[1] for x in to_do_list]
print(to_do_list)


# notes = input()
# dict_with_notes = {}
#
# while notes != "End":
#     key, value = notes.split("-")
#     dict_with_notes[int(key)] = value
#     notes = input()
#
# dict_with_notes = dict(sorted(dict_with_notes.items()))
# to_do_list = list(dict_with_notes.values())
# print(to_do_list)
