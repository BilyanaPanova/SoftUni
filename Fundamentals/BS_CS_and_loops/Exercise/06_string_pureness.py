number_of_words = int(input())

for _ in range(number_of_words):
    word = input()
    flag = False
    for letter in word:
        if letter == "," or letter == "." or letter == "_":
            flag = True
            break
    if flag:
        print(f"{word} is not pure!")
    else:
        print(f"{word} is pure.")
