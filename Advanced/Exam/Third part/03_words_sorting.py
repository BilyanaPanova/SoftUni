def words_sorting(*words):
    words_dict = {}
    for word in words:
        words_dict[word] = sum([ord(x) for x in word])
    if sum(words_dict.values()) % 2 == 0:
        words_dict = dict(sorted(words_dict.items(), key=lambda x: x[0]))
    else:
        words_dict = dict(sorted(words_dict.items(), key=lambda x: -x[1]))

    result = ""
    for key, value in words_dict.items():
        result += f"{key} - {value}\n"
    return result.strip()
