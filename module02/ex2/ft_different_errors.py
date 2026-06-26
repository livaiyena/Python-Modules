def garden_operations(operation_number) -> int:
    match operation_number:
        case 0:
            int("abc")
        case 1:
            1 / 0
        case 2:
            open("/non/existent/file")
        case 3:
            print("abc" + 5)
    return 0


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    for i in range(5):
        try:
            print(f"Testing operation {i}...")
            garden_operations(i)
            print("Operation completed successfully")
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except TypeError as e:
            print(f"Caught TypeError: {e}")
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
