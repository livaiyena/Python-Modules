class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(
            f"{self.name.capitalize()}:"
            f" {self.height}cm, {self.age} days old"
            )


if __name__ == "__main__":
    info_rose = Plant("rose", 25, 30)
    info_sunflower = Plant("sunflower", 80, 45)
    info_cactus = Plant("cactus", 15, 120)
    print("=== Garden Plant Registry ===")
    info_rose.show()
    info_sunflower.show()
    info_cactus.show()
