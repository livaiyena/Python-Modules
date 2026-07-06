import sys


def main() -> None:
    print("=== Player Score Analytics ===")

    _, *scores_raw = sys.argv
    scores: list[int] = []
    for score in scores_raw:
        try:
            temp = int(score)
            scores = scores + [temp]
        except ValueError:
            print(f"Invalid parameter: '{score}'")
    if not scores:
        print("No scores provided. "
              "Usage: python3 ft_score_analytics.py "
              "<score1> <score2> ...")
        return

    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {sum(scores) / len(scores):.1f}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    main()
