def sum_numbers(my_list: list, first: int, last: int) -> float:
    if first < 0:
        first = 0
    if last > len(my_list) - 1:
        last = len(my_list) - 1
    return sum(my_list[first:last + 1])


if __name__ == '__main__':
    nums = [0, 3, 4, 6, 2, 5, 6]
    print(sum_numbers(nums, 4, 4))
