banned_word = input().split(", ")
text = input()

for word in banned_word:

    while word in text:
        replace_word = len(word) * "*"
        text = text.replace(word,replace_word)

print(text)