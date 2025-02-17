dict_synonyms = {}
count_of_lines = int(input())

for line in range(count_of_lines):
    word = input()
    synonyms = input()

    if word not in dict_synonyms:
        dict_synonyms[word] = [synonyms]
    else:
        dict_synonyms[word].append(synonyms)

for word in dict_synonyms:
    print(f"{word} - {', '.join(dict_synonyms[word])}")
