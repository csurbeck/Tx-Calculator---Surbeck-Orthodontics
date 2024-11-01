from global_vars import GlobalVariables


def calculate_cost():
    length = int((GlobalVariables.tx_length[:2]).strip())

    if GlobalVariables.tx_plan == "Phase I – One Arch":
        base = 1200
        GlobalVariables.cost = (base + (length * 250))
        if GlobalVariables.records == "Records": GlobalVariables.cost += 440
    elif GlobalVariables.tx_plan == "Phase I – Two Arches":
        base = 1464
        GlobalVariables.cost = (base + (length * 300))
        if GlobalVariables.records == "Records": GlobalVariables.cost += 440
    elif GlobalVariables.tx_plan == "Limited Treatment":
        base = 1597
        GlobalVariables.cost = (base + (length * 300))
        if GlobalVariables.records == "Records": GlobalVariables.cost += 550
    elif GlobalVariables.tx_plan == "Full Treatment – Adult":
        base = 2130
        GlobalVariables.cost = (base + (length * 466))
    elif GlobalVariables.tx_plan == "Full Treatment – Adult, Surgery":
        base = 2556
        GlobalVariables.cost = (base + (length * 559.2))
    elif GlobalVariables.tx_plan == "Full Treatment – Child, Surgery":
        base = 2556
        GlobalVariables.cost = (base + (length * 478.80))
    else:
        base = 2130
        GlobalVariables.cost = (base + (length * 399))

    if GlobalVariables.tx_material == "Clear Brackets":
        GlobalVariables.cost += 477