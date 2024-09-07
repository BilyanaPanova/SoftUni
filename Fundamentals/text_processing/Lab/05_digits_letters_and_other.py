some_string = input()

digits = [x for x in some_string if x.isdigit()]
letters = [x for x in some_string if x.isalpha()]
other_chars = [x for x in some_string if not x.isalnum()]

print(*digits, sep="")
print(*letters, sep="")
print(*other_chars, sep="")
