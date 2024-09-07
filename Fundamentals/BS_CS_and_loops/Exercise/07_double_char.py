word = ''
while True:
    enter = input()

    if enter == "End":
        break
    elif enter == "SoftUni":
        continue
    else:
        for letter in enter:
            word += 2 * letter

    print(word)
    word = ''
