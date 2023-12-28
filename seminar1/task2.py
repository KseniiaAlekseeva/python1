def primeNumber(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
        return True


while True:
    print("Enter number: ")
    num = int(input())
    if num > 0 and num <= 1e5:
        if primeNumber(num):
            print(f"Number {num} is prime.")
        else:
            print(f"Number {num} is not prime.")
        break
