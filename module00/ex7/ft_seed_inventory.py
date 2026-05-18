def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seedUnits = ("packets", "grams", "area")
    if unit not in seedUnits:
        print("Unknown unit type")
        return
    unitUsage = ""
    match unit:
        case "packets":
            unitUsage = f"{quantity} packets available"
        case "grams":
            unitUsage = f"{quantity} grams total"
        case "area":
            unitUsage = f"covers {quantity} square meters"
    print(f"{seed_type.capitalize()} seeds: {unitUsage}")
