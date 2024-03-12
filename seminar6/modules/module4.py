import random

__all__ = ['is_good_position', 'find_good_position']


def is_good_position(position: list[list[int]]) -> bool:
    n = 8
    x = []
    y = []

    for i in range(n):
        x.append(position[i][0])
        y.append(position[i][1])
    flag = True
    for i in range(n):
        for j in range(i + 1, n):
            if abs(x[i] - x[j]) == abs(y[i] - y[j]):
                flag = False
    return flag


def find_good_position(count_good: int):
    pos_list = []
    position = []
    n = 8
    count = 1
    count_iter = 0
    while count <= count_good:
        count_iter += 1
        i = 0
        while i < n:
            x = random.randint(1, 8)
            y = random.randint(1, 8)
            if [x, y] not in position:
                position.append([x, y])
                i += 1
        if is_good_position(position):
            print(position, 'iter = ', count_iter)
            pos_list.append(list(position))
            count += 1
        position.clear()
    return pos_list


if __name__ == '__main__':
    print(is_good_position([[1, 1], [5, 2], [8, 3], [6, 4], [3, 5], [7, 6], [2, 7], [4, 8]]))
    print(is_good_position([[2, 1], [5, 2], [8, 3], [6, 4], [3, 5], [7, 6], [2, 7], [4, 8]]))
    find_good_position(4)
