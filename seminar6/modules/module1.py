import random
from sys import argv

__all__ = ['guess_number']


def guess_number(lower_limit: int = 0, upper_limit: int = 10, max_try: int = 1) -> bool:
    num = random.randint(lower_limit, upper_limit)
    print(f"Secret number - {num}")
    for i in range(max_try):
        cur_num = int(input("Enter the number: "))
        if cur_num == num:
            print(f"You win! Attempt - {i + 1}")
            return True
        else:
            if num > cur_num:
                print(f"More... Attempt - {i + 1}")
            else:
                print(f"Less... Attempt - {i + 1}")
            if i + 1 == max_try:
                print("All attempts is over. You loose.")
                return False


if __name__ == '__main__':
    args = [int(i) for i in argv[1:]]
    lower_limit = 0
    upper_limit = 50
    max_try = 1
    if len(args) < 1:
        print('Not enough arguments')
    if len(args) in (1, 2, 3):
        lower_limit = args[0]
    if len(args) in (1, 2, 3):
        upper_limit = args[1]
    if len(args) == 3:
        max_try = args[2]
        pass
    print(args)
    print(guess_number(lower_limit, upper_limit, max_try))
