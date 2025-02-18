def draw_cards(*args, **kwargs):
    monster = []
    spell = []
    for name, type in args:
        if type == "monster":
            monster.append("  ***" + name)
        else:
            spell.append("  $$$" + name)
    for key, value in kwargs.items():
        if value == "monster":
            monster.append("  ***" + key)
        else:
            spell.append("  $$$" + key)

    result = ""
    if monster:
        result += "Monster cards:\n"
        result += "\n".join(sorted(monster,reverse=True))
        result += "\n"
    if spell:
        result += "Spell cards:\n"
        result += "\n".join(sorted(spell))

    return result


print(draw_cards(("brave attack", "monster"), ("freeze", "monster"), lightning_bolt="monster", fireball="spell",))
