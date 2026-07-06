import random
from typing import Generator


PLAYERS: list[str] = ["alice", "bob", "charlie", "dylan"]
ACTIONS: list[str] = [
    "run", "eat", "sleep", "grab", "move",
    "climb", "swim", "release", "use",
]


def gen_event() -> Generator[tuple[str, str], None, None]:
    while True:
        name = random.choice(PLAYERS)
        action = random.choice(ACTIONS)
        yield (name, action)


def consume_event(
    event_list: list[tuple[str, str]],
) -> Generator[tuple[str, str], None, None]:
    while len(event_list) > 0:
        idx = random.randint(0, len(event_list) - 1)
        event = event_list[idx]
        event_list.pop(idx)
        yield event


def main() -> None:
    print("=== Game Data Stream Processor ===")

    generator = gen_event()
    for i in range(1000):
        event = next(generator)
        print(f"Event {i}: Player {event[0]}"
              f" did action {event[1]}")

    event_gen = gen_event()
    event_list: list[tuple[str, str]] = []
    for _ in range(10):
        event_list = event_list + [next(event_gen)]
    print(f"Built list of 10 events: {event_list}")

    for event in consume_event(event_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {event_list}")


if __name__ == "__main__":
    main()
