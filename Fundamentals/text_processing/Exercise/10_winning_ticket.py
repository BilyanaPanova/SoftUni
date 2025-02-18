import re

symbols = "\@+|\#+|\^+|\$+"
collection_of_tickets = re.split(", | ", input())
collection_of_tickets = [x for x in collection_of_tickets if x != ""]

for ticket in collection_of_tickets:
    if len(ticket) == 20:
        first_half = [x for x in re.findall(symbols, ticket[:10]) if len(x) >= 6]
        second_half = [x for x in re.findall(symbols, ticket[10:]) if len(x) >= 6]
    else:
        print("invalid ticket")
        continue

    if any([x for x in ticket if x in ("@", "#", "$", "^")]) and first_half and second_half:
        first_half = first_half[0]
        second_half = second_half[0]
        if len(first_half) == len(second_half) == 10 and first_half[0] == second_half[0]:
            print(f'ticket "{ticket}" - {len(first_half)}{first_half[0]} Jackpot!')
            continue
        elif len(first_half) >= 6 and len(second_half) >= 6 and first_half[0] == second_half[0]:
            min_length = min(len(first_half), len(second_half))
            print(f'ticket "{ticket}" - {min_length}{first_half[0]}')
            continue

    print(f'ticket "{ticket}" - no match')
