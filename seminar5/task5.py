def check_prime(n: int) -> bool:
    if n == 0 or n == 1 or n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def gen_prime_nums(n: int):
    count = 0
    i = 2
    while count < n:
        if check_prime(i):
            yield i
            count += 1
        i += 1


if __name__ == '__main__':
    for i in gen_prime_nums(10):
        print(i)
