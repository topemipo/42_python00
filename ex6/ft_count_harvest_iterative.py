def ft_count_harvest_iterative() -> None:
    days = 1 + int(input("Days until harvest: "))

    for i in range(1, days):
        print(f"Day {i}")
    print("Harvest time!")
