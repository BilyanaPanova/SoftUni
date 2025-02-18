def add_songs(*songs):
    dict_info = {}

    for song, lyrics in songs:
        if song not in dict_info.keys():
            dict_info[song] = ""
        if lyrics:
            dict_info[song] += "\n".join(lyrics) + "\n"

    result = ""
    for s,l in dict_info.items():
        result += f"- {s}\n"
        if l:
            result += f"{l}"
    return result.strip()


print(add_songs(
    ("Beat It", []),
    ("Beat It",
     ["Just beat it (beat it), beat it (beat it)",
      "No one wants to be defeated"]),
    ("Beat It", []),
    ("Beat It",
     ["Showin' how funky and strong is your fight",
      "It doesn't matter who's wrong or right"]),
))