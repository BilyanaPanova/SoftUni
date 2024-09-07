import string

text = input()

number_list = [int(x) for x in text if x in string.digits]
non_num_list = [x for x in text if x not in string.digits]
take_list = number_list[0::2]
skip_list = number_list[1::2]
take_index = 0
taken_string = []
skip_string = []

while True:
    if len(non_num_list) == 0:
        break
    if take_index >= len(take_list):
        break

    taken_string.extend(non_num_list[0:take_list[take_index]])
    non_num_list = non_num_list[take_list[take_index]:]
    skip_string.extend(non_num_list[0:skip_list[take_index]])
    non_num_list = non_num_list[skip_list[take_index]:]
    take_index += 1

print(*taken_string,sep="")
