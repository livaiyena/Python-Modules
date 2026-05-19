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
        self._height += 1.1
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


class Flower (Plant):
    is_bloomed = 0

    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super.__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        Flower.is_bloomed = 1

    def show(self) -> None:
        super().show
        print(f" Color: {self.color}")
        if Flower.is_bloomed:
            print(f" {self.name.capitalize()} is blooming beautifully")
        else:
            print(f" {self.name.capitalize()} has not bloomed yet")


class Tree (Plant):
    def __init__(
            self, name: str, height: float,
            age: int, trunk_diameter: float) -> None:
        super.__init__(name, height, age)
        self.trunk_diameter = round(float(trunk_diameter))

    def produce_shade(self) -> None:
        print(f"Tree {self.name} produces a shade of {self._height}cm long"
              f" and {self.trunk_diameter}wide.")

    def show(self) -> None:
        super().show
        print(f" Trunk diameter: {self.trunk_diameter}cm")


class Vegetable (Plant):
    def __init__(
            self, name: str, height: float,
            age: int, harvest_season: str,
            nutritional_value: int) -> None:
        super.__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def age(self) -> None:
        super.age
        self.nutritional_value += 1

    def grow(self) -> None:
        super().grow()

    def show(self) -> None:
        super().show
        print(f" Harvest season: {self.harvest_season}"
              f"\n Nutritional value: {self.nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    
    print("--- Flower")
    rose = Flower("rose", 15.0, 10, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()

    print("\n--- Tree")
    oak = Tree("oak", 200.0, 365, 5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()

    print("\n--- Vegetable")
    tomato = Vegetable("tomato", 5.0, 10, "April", 0)
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for _ in range(20):
        tomato.grow()
        tomato.age()
    tomato.show()
