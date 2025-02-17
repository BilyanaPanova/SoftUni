import re

key_word = input()
print_words = []
input_string = input()

while input_string != "end":
    match = re.match(r'^[A-Z].+[\.\!\?]$', input_string)

    if match:
        string = re.findall(r"[A-Za-z]+", match.group())
        for word in string:
            if word.count(key_word[0]) >= int(key_word[1:]):
                print_words.append(word)

    input_string = input()
print(*print_words, sep=", ")
