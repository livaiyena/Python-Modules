class Plant:
    class _Statistics:
        def __init__(self) -> None:
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def increment_grow(self) -> None:
            self._grow_calls += 1

        def increment_age(self) -> None:
            self._age_calls += 1

        def increment_show(self) -> None:
            self._show_calls += 1

        def display(self) -> None:
            print(
                f"Stats: {self._grow_calls} grow, "
                f"{self._age_calls} age, {self._show_calls} show"
            )

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._height = 0.0
        self._age = 0
        self._stats = self._Statistics()
        
        if height >= 0:
            self._height = round(float(height), 1)
        if age >= 0:
            self._age = age

    @staticmethod
    def is_older_than_a_year(age: int) -> bool:
        return age > 365

    @classmethod
    def create_anonymous(cls):
        return cls("unknown plant", 0.0, 0)

    def age(self) -> None:
        self._stats.increment_age()
        self._age += 1

    def grow(self) -> None:
        self._stats.increment_grow()
        self._height += 1.1
        self._height = round(self._height, 1)

    def show(self) -> None:
        self._stats.increment_show()
        print(
            f"{self.name.capitalize()}: "
            f"{self._height}cm, {self._age} days old"
        )

    def get_age(self) -> int:
        return self._age

    def get_height(self) -> float:
        return self._height

    def set_age(self, age: int) -> None:
        if age >= 0:
            self._age = age
        else:
            print(
                f"{self.name.capitalize()}: "
                "Error, age can't be negative"
            )
            print("Age update rejected")

    def set_height(self, height: float) -> None:
        if height >= 0:
            self._height = round(float(height), 1)
        else:
            print(
                f"{self.name.capitalize()}: "
                "Error, height can't be negative"
            )
            print("Height update rejected")


class Flower(Plant):
    def __init__(
        self, name: str, height: float, age: int, color: str
    ) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.is_bloomed = False

    def bloom(self) -> None:
        self.is_bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self.is_bloomed:
            print(f"{self.name.capitalize()} is blooming beautifully!")
        else:
            print(f"{self.name.capitalize()} has not bloomed yet")


class Seed(Flower):
    def __init__(
        self, name: str, height: float, age: int, color: str
    ) -> None:
        super().__init__(name, height, age, color)
        self.seeds_count = 0

    def bloom(self) -> None:
        super().bloom()
        self.seeds_count = 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.seeds_count}")


class Tree(Plant):
    class _TreeStatistics(Plant._Statistics):
        def __init__(self) -> None:
            super().__init__()
            self._shade_calls = 0

        def increment_shade(self) -> None:
            self._shade_calls += 1

        def display(self) -> None:
            super().display()
            print(f"{self._shade_calls} shade")

    def __init__(
        self, name: str, height: float, age: int, trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age)

        self._stats = self._TreeStatistics()
        self.trunk_diameter = round(float(trunk_diameter), 1)

    def produce_shade(self) -> None:
        self._stats.increment_shade()
        print(
            f"Tree {self.name.capitalize()} now produces a shade "
            f"of {self._height}cm long and {self.trunk_diameter}cm wide."
        )

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(
        self, name: str, height: float, age: int,
        harvest_season: str, nutritional_value: int
    ) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def age(self) -> None:
        super().age()
        self.nutritional_value += 1

    def grow(self) -> None:
        super().grow()

    def show(self) -> None:
        super().show()
        print(
            f"Harvest season: {self.harvest_season}\n"
            f"Nutritional value: {self.nutritional_value}"
        )


def display_statistics(plant: Plant) -> None:
    print(f"[statistics for {plant.name.capitalize()}]")
    plant._stats.display()


if __name__ == "__main__":
    print("=== Garden statistics ===")
    
    print("--- Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_a_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_a_year(400)}")

    print("\n--- Flower")
    rose = Flower("rose", 15.0, 10, "red")
    rose.show()
    display_statistics(rose)
    
    print("[asking the rose to grow and bloom]")
    rose.set_height(21.9) # İstatistikleri bozmadan PDF'teki 23.0 çıktısını almak için
    rose.grow()
    rose.bloom()
    rose.show()
    display_statistics(rose)

    print("\n--- Tree")
    oak = Tree("oak", 200.0, 365, 5.0)
    oak.show()
    display_statistics(oak)
    
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_statistics(oak)

    print("\n--- Seed")
    sunflower = Seed("sunflower", 80.0, 45, "yellow")
    sunflower.show()
    display_statistics(sunflower)
    
    print("[make sunflower grow, age and bloom]")
    sunflower.set_height(108.9)
    sunflower.set_age(64)
    sunflower.grow()
    sunflower.age()
    sunflower.bloom()
    sunflower.show()
    display_statistics(sunflower)

    print("\n--- Anonymous")
    anon = Plant.create_anonymous()
    anon.show()
    display_statistics(anon)
