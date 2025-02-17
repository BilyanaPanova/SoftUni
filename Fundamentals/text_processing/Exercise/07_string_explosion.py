text = input()
new_text = ""
explosion = 0

for index in range(len(text)):
    if explosion > 0 and text[index] != ">":
        explosion -= 1
    elif text[index] == ">":
        new_text += text[index]
        explosion += int(text[index + 1])
    else:
        new_text += text[index]

print(new_text)
