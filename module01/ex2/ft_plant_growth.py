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
    info_rose = Plant("rose", 25, 30)
    print("=== Garden Plant Registry ===")
    info_rose.show()
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        info_rose.grow()
        info_rose.age()
        print(f"{info_rose.name.capitalize()}:", end=" ")
        print(f"{info_rose.height}cm, {info_rose.current_age} days old")
    print(f"Growth this week: {info_rose.plant_growth}cm")
