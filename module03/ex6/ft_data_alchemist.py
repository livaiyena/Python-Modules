import random


def main() -> None:
    print("=== Game Data Alchemist ===")

    players: list[str] = [
        "Alice", "bob", "Charlie", "dylan",
        "Emma", "Gregory", "john", "kevin", "Liam",
    ]
    print(f"Initial list of players: {players}")

    all_caps: list[str] = [n.capitalize() for n in players]
    print(f"New list with all names capitalized: {all_caps}")

    only_caps: list[str] = [n for n in players if n[0].isupper()]
    print(f"New list of capitalized names only: {only_caps}")

    scores: dict[str, int] = {
        n: random.randint(0, 1000) for n in all_caps
    }
    print(f"Score dict: {scores}")

    avg = round(sum(scores.values()) / len(scores), 2)
    print(f"Score average is {avg}")

    high: dict[str, int] = {
        n: s for n, s in scores.items() if s > avg
    }
    print(f"High scores: {high}")


if __name__ == "__main__":
    main()
