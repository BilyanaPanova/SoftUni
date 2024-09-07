# import re
#
# string = [x.start() for x in re.finditer(r"[A-Z]",input())]
# print(string)
string = [index for index, x in enumerate(input()) if x.isupper()]
print(string)
