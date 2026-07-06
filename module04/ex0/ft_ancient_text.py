import sys
import typing


def read_file(filename: str) -> None:
    print(f"Accessing file '{filename}'")
    fd: typing.IO[str]
    try:
        fd = open(filename, "r")
    except OSError as e:
        print(f"Error opening file '{filename}': {e}")
        return
    content = fd.read()
    print("---")
    print(content, end="")
    print("---")
    fd.close()
    print(f"File '{filename}' closed.")


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    print("=== Cyber Archives Recovery ===")
    read_file(sys.argv[1])


if __name__ == "__main__":
    main()
