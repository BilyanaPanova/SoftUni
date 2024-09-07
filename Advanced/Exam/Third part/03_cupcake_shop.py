def stock_availability(inventory:list,case:str,*args):
    if case == "delivery":
        inventory.extend([*args])
    elif case == "sell":
        if not args:
            inventory = inventory[1:]
        for a in args:
            if isinstance(a,int):
                a = int(a)
                inventory = inventory[a:]
            else:
                inventory = [el for el in inventory if el != a]
    return inventory
