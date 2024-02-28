def sort_list(my_list: list) -> list:
    for i in range(1, len(my_list)):
        flag = False
        for j in range(0, len(my_list) - i):
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
                flag = True
        if not flag:
            break
    return my_list


if __name__ == '__main__':
    my_list = [2, 5, 1, 7, 9, 0, 1, 4]
    print(sort_list(my_list))
