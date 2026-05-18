def ft_water_reminder() -> None:
    lastWatering = int(input("Day since last watering: "))
    if lastWatering > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
