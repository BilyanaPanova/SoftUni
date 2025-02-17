def char_in_range(start, end):
    all_char = ""
    for char in range(ord(start) + 1, ord(end)):
        all_char += chr(char) + " "
    return all_char[0:-1]


start_char = input()
end_char = input()
print(char_in_range(start_char, end_char))
