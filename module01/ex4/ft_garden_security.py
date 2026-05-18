class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._height = 0.0
        self._age = 0
        if height >= 0:
            self._height = round(float(height), 1)
        if age >= 0:
            self._age = age

    def age(self) -> None:
        self._age += 1

    def grow(self) -> None:
        self._height += 0.8
        self._height = round(self._height, 1)

    def show(self) -> None:
        print(
            f"{self.name.capitalize()}:"
            f" {self._height}cm, {self._age} days old"
            )

    def get_age(self) -> None:
        return self._age

    def get_height(self) -> None:
        return self._height

    def set_age(self, age) -> None:
        if age >= 0:
            self._age = age
        else:
            print(f"{self.name.capitalize()}: Error, age can't be negative")
            print("Age update rejected")

    def set_height(self, height) -> None:
        if height >= 0:
            self._height = round(float(height), 1)
        else:
            print(f"{self.name.capitalize()}: Error, height can't be negative")
            print("Height update rejected")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant1 = Plant("rose", 15.0, 10)
    print("Plant created:", end=" ")
    plant1.show()
    print()
    plant1.set_height(25)
    print("Height updated: 25 cm")
    plant1.set_age(30)
    print("Age updated: 30 days")
    print()
    plant1.set_height(-5)
    plant1.set_age(-5)
    print()
    print("Current state:", end=" ")
    plant1.show()
