import sys


def main() -> None:
    print("=== Inventory System Analysis ===")

    _, *args = sys.argv
    inventory: dict[str, int] = {}

    for arg in args:
        if ":" not in arg:
            print(f"Error - invalid parameter '{arg}'")
            continue
        parts = arg.split(":")
        if len(parts) != 2:
            print(f"Error - invalid parameter '{arg}'")
            continue
        item_name = parts[0]
        quantity_str = parts[1]
        if item_name in inventory:
            print(f"Redundant item '{item_name}' - discarding")
            continue
        try:
            quantity = int(quantity_str)
        except ValueError as e:
            print(f"Quantity error for '{item_name}': {e}")
            continue
        inventory[item_name] = quantity

    if not inventory:
        print("At the beginning of the game, "
              "your inventory is usually empty ;)")
        return

    print(f"Got inventory: {inventory}")

    item_list: list[str] = list(inventory.keys())
    print(f"Item list: {item_list}")

    total = sum(inventory.values())
    print(f"Total quantity of the "
          f"{len(inventory)} items: {total}")

    for item, qty in inventory.items():
        pct = round(qty / total * 100, 1)
        print(f"Item {item} represents {pct}%")

    most_name = ""
    most_qty = -1
    least_name = ""
    least_qty = total + 1
    for item, qty in inventory.items():
        if qty > most_qty:
            most_qty = qty
            most_name = item
        if qty < least_qty:
            least_qty = qty
            least_name = item
    print(f"Item most abundant: "
          f"{most_name} with quantity {most_qty}")
    print(f"Item least abundant: "
          f"{least_name} with quantity {least_qty}")

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")

    print("At the beginning of the game, "
          "your inventory is usually empty ;)")


if __name__ == "__main__":
    main()
