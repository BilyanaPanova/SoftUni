first_word = input()
second_word = input()
first_word_list = list(first_word)

for index in range(len(first_word)):
    if first_word_list[index] != second_word[index]:
        first_word_list[index] = second_word[index]
        print("".join(first_word_list))

