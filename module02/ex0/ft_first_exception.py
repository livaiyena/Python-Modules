def input_temperature(temp_str: str) -> int:
    print(f"Input data is '{temp_str}'")
    temp_int = int(temp_str)
    return temp_int


def test_temperature() -> None:
    print("=== Garden Temperature ===")
    data_set = ("25", "abc")
    for temp_str in data_set:
        print()
        try:
            temp_int = input_temperature(temp_str)
            print(f"Temperature is now {temp_int}°C")
        except ValueError as e:
            print(f"Caught input_temperature error: {e}")
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
