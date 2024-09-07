import re


def find_happy_emoji(string):
    happy_emoji_pattern = r".?([:{1}|;{1}][\)\]D\}\*]{1}).?|.?([\(\*c\[]{1}[:;]{1}).?"
    matches = re.findall(happy_emoji_pattern, string)
    return [x[0] for x in matches]


def find_sad_emoji(string):
    sad_emoji_pattern = r".?([\:{1}|\;{1}][\(\[\{c]{1}).?|.?([\)\]D]{1}[\:|\;]{1}).?"
    matches = re.findall(sad_emoji_pattern, string)
    return [x[0] for x in matches]


def happiness_index(string):
    list_with_happy_emoji = find_happy_emoji(string)
    list_with_sad_emoji = find_sad_emoji(string)
    happiness_i = len(list_with_happy_emoji) / len(list_with_sad_emoji)
    happiness_emoji = ""

    if happiness_i >= 2:
        happiness_emoji = ":D"
    elif happiness_i > 1:
        happiness_emoji = ":)"
    elif happiness_i == 1:
        happiness_emoji = ":|"
    else:
        happiness_emoji = ":("

    return len(list_with_happy_emoji), len(list_with_sad_emoji), happiness_i, happiness_emoji


some_string = input()

happy_count, sad_count, happy_index, happy_emoji = happiness_index(some_string)

print(f"Happiness index: {happy_index:.2f} {happy_emoji}")
print(f"[Happy count: {happy_count}, Sad count: {sad_count}]")
