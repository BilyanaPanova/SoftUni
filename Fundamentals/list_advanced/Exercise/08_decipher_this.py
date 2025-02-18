import re

secret_message = input().split()
for word in secret_message:
    digit = re.findall(r"\d+", word)
    digit = int(digit[0])
    word = [x for x in word if x.isalpha()]
    # word[0], word[- 1] = word[- 1], word[0]
    # new_word = chr(digit) + "".join(word)
    new_word = chr(digit) + word[-1] + "".join(word[1:-1]) + word[0]
    print(new_word, end=" ")
