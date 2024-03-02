# Создайте функцию генератор чисел Фибоначчи

def gen_fibonachi(n):
    i, j = 0, 1
    for _ in range(n):
        yield i
        i, j = j, i + j


if __name__ == '__main__':
    num = 10
    for i in gen_fibonachi(num):
        print(i, end='\t')
