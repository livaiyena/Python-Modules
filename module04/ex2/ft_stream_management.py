import sys
import typing


def read_file(filename: str) -> str:
    print(f"Accessing file '{filename}'")
    fd: typing.IO[str]
    try:
        fd = open(filename, "r")
    except OSError as e:
        sys.stderr.write(
            f"[STDERR] Error opening file '{filename}': {e}\n"
        )
        sys.stderr.flush()
        return ""
    content = fd.read()
    print("---")
    print(content, end="")
    print("---")
    fd.close()
    print(f"File '{filename}' closed.")
    return content


def transform_data(content: str) -> str:
    lines = content.split("\n")
    result: list[str] = []
    for line in lines:
        if line:
            result.append(line + "#")
    return "\n".join(result) + "\n"


def save_file(filename: str, content: str) -> None:
    print(f"Saving data to '{filename}'")
    fd: typing.IO[str]
    try:
        fd = open(filename, "w")
    except OSError as e:
        sys.stderr.write(
            f"[STDERR] Error opening file '{filename}': {e}\n"
        )
        sys.stderr.flush()
        print("Data not saved.")
        return
    fd.write(content)
    fd.close()
    print(f"Data saved in file '{filename}'.")


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_stream_management.py <file>")
        return
    print("=== Cyber Archives Recovery & Preservation ===")
    content = read_file(sys.argv[1])
    if not content:
        return
    transformed = transform_data(content)
    print("Transform data:")
    print("---")
    print(transformed, end="")
    print("---")
    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()
    new_name = sys.stdin.readline().strip()
    if not new_name:
        print("Not saving data.")
        return
    save_file(new_name, transformed)


if __name__ == "__main__":
    main()
