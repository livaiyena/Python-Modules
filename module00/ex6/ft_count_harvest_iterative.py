def ft_count_harvest_iterative() -> None:
    untilHarvest = int(input("Days until harvest: "))
    for i in range(1, untilHarvest + 1):
        print("Day", i)
    print("Harvest time!")
