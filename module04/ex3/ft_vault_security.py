def secure_archive(
    filename: str,
    mode: str = "r",
    content: str = "",
) -> tuple[bool, str]:
    try:
        with open(filename, mode) as fd:
            if mode == "r":
                data = fd.read()
                return (True, data)
            else:
                fd.write(content)
                return (True,
                        "Content successfully written to file")
    except OSError as e:
        return (False, str(e))


def main() -> None:
    print("=== Cyber Archives Security ===")

    print("Using 'secure_archive' to read"
          " from a nonexistent file:")
    result = secure_archive("/not/existing/file")
    print(result)

    print("Using 'secure_archive' to read"
          " from an inaccessible file:")
    result = secure_archive("/etc/shadow")
    print(result)

    print("Using 'secure_archive' to read"
          " from a regular file:")
    result = secure_archive("ancient_fragment.txt")
    print(result)

    print("Using 'secure_archive' to write"
          " previous content to a new file:")
    if result[0]:
        result = secure_archive(
            "vault_copy.txt", "w", result[1]
        )
    print(result)


if __name__ == "__main__":
    main()
