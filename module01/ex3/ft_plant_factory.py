class Plant:
    def __init__(self, name: str, height: float, current_age: int) -> None:
        self.name = name
        self.height = round(float(height), 1)
        self.current_age = current_age
        self.plant_growth = 0.0

    def age(self) -> None:
        self.current_age += 1

    def grow(self) -> None:
        self.height += 0.8
        self.plant_growth += 0.8
        self.height = round(self.height, 1)
        self.plant_growth = round(self.plant_growth, 1)

    def show(self) -> None:
        print(
            f"{self.name.capitalize()}:"
            f" {self.height}cm, {self.current_age} days old"
            )


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    plant1 = Plant("rose", 25.0, 30)
    plant2 = Plant("oak", 200.0, 365)
    plant3 = Plant("cactus", 5.0, 90)
    plant4 = Plant("sunflower", 80.0, 45)
    plant5 = Plant("fern", 15.0, 120)
    print("Created:", end=" ")
    plant1.show()
    print("Created:", end=" ")
    plant2.show()
    print("Created:", end=" ")
    plant3.show()
    print("Created:", end=" ")
    plant4.show()
    print("Created:", end=" ")
    plant5.show()
