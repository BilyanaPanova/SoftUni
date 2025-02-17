text = list(input())
vowels = ['a', 'o', 'u', 'e', 'i']
text = [x for x in text if x.lower() not in vowels]
print("".join(text))
