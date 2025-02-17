import re

some_string = input()
while some_string != "end":

    if "<a" in some_string and "</a>" in some_string:
        some_string = re.sub("<a", "[URL", some_string)
        some_string = re.sub("</a", "[/URL", some_string)
        some_string = re.sub(">", "]", some_string)

    print(some_string)
    some_string = input()
