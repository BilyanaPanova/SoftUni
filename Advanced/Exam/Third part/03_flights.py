def flights(*args):
    destinations = {}
    for i in range(0, len(args) + 1, 2):
        if args[i] == "Finish":
            return destinations
        if args[i] not in destinations:
            destinations[args[i]] = 0
        destinations[args[i]] += int(args[i + 1])


