def movie_organizer(*args):
    dict_movie = {}
    for name, genre in args:
        if genre not in dict_movie:
            dict_movie[genre] = []
        dict_movie[genre].append(name)
    dict_movie = dict(sorted(dict_movie.items(), key=lambda x: (-len(x[1]), x[0])))
    result = ""
    for key, value in dict_movie.items():
        result += f"{key} - {len(value)}\n"
        for v in sorted(value):
            result += f"* {v}\n"
    return result

