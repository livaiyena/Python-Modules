import sys


def main() -> None:
    print("=== Command Quest ===")

    prog_name, *args = sys.argv
    print(f"Program name: {prog_name}")

    if not args:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {len(args)}")
        i = 1
        for arg in args:
            print(f"Argument {i}: {arg}")
            i += 1

    print(f"Total arguments: {len(sys.argv)}\n")


if __name__ == "__main__":
    main()
