import random


ALL_ACHIEVEMENTS: list[str] = [
    "First Steps", "Master Explorer", "Boss Slayer",
    "Collector Supreme", "Speed Runner", "Strategist",
    "Untouchable", "World Savior", "Crafting Genius",
    "Survivor", "Unstoppable", "Treasure Hunter",
    "Sharp Mind", "Hidden Path Finder",
]


def gen_player_achievements() -> set[str]:
    count = random.randint(4, 9)
    return set(random.sample(ALL_ACHIEVEMENTS, count))


def main() -> None:
    print("=== Achievement Tracker System ===")

    players: dict[str, set[str]] = {
        "Alice": gen_player_achievements(),
        "Bob": gen_player_achievements(),
        "Charlie": gen_player_achievements(),
        "Dylan": gen_player_achievements(),
    }

    for name, achievements in players.items():
        print(f"Player {name}: {achievements}")

    all_achievements: set[str] = set()
    for achievements in players.values():
        all_achievements = all_achievements.union(achievements)
    print(f"All distinct achievements: {all_achievements}")

    common: set[str] = set(ALL_ACHIEVEMENTS)
    for achievements in players.values():
        common = common.intersection(achievements)
    print(f"Common achievements: {common}")

    for name, achievements in players.items():
        unique = achievements
        for other_name, other_ach in players.items():
            if other_name != name:
                unique = unique.difference(other_ach)
        print(f"Only {name} has: {unique}")

    for name, achievements in players.items():
        missing = all_achievements.difference(achievements)
        print(f"{name} is missing: {missing}")


if __name__ == "__main__":
    main()
