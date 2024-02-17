MAX_NUM = 1e5


def prime_number(n):
    if n == 0 or n == 1 or n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


while True:
    num = int(input("Enter number: "))
    if 0 < num <= MAX_NUM:
        if prime_number(num):
            print(f"Number {num} is prime.")
        else:
            print(f"Number {num} is not prime.")
        break
