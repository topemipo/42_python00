# # Using a nested helper function inside your main function
# def ft_count_harvest_recursive() -> None:
#     harvest_days = 1 + int(input("Days until harvest: "))
#     current_day = 1
#     def helper() -> None:
#         nonlocal current_day 
#         if current_day in range(1, harvest_days):
#             print(f"Day {current_day}")
#             current_day += 1
#             helper()
#     helper()
#     print("Harvest time!")


# Using default parameter values
def ft_count_harvest_recursive(current_day=1, harvest_day=None) -> None:
    if harvest_day == None:
        harvest_day = 1 + int(input("Days until harvest: "))
    if current_day in range(1, harvest_day):
        print(f"Day {current_day}")
        current_day += 1
        ft_count_harvest_recursive(current_day, harvest_day)
    else:
        print("Harvest time!")
    

# # Using a separate helper function called by your main function
# def helper(x:int, y: int) -> None:
#     if x in range(1, y):
#         print(f"Day {x}")
#         helper(x + 1, y)


# def ft_count_harvest_recursive() -> None:
#     harvest_days = 1 + int(input("Days until harvest: "))
#     current_day = 1
#     helper(current_day, harvest_days)
#     print("Harvest time!")
