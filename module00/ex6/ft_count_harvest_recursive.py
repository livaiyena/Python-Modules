def ft_count_harvest_recursive() -> None:
    untilHarvest = int(input("Days until harvest: "))
    i = 1

    def ft_count_recursive(i: int) -> None:
        print("Day", i)
        if i == untilHarvest:
            print("Harvest time!")
            return
        i += 1
        ft_count_recursive(i)
    ft_count_recursive(i)
