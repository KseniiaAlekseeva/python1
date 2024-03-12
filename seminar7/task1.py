from random import randint, random


def gen_pair(min_lim: int, max_lim: int) -> tuple:
    a = randint(-1000, 1000)
    b = random() * (max_lim - min_lim) + min_lim
    return a, b


def print_nums(num_lines: int, name: str) -> None:
    with open(name, 'a', encoding='utf-8') as f:
        for i in range(num_lines):
            a, b = gen_pair(-1000, 1000)
            print(f'{a} | {b}', file=f)


if __name__ == '__main__':
    print_nums(10, 'file1.txt')
