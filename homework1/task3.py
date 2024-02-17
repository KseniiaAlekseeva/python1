import random

LOWER_LIMIT = 0
UPPER_LIMIT = 50
MAX_TRY = 10


def guess_number(max_try):
    for i in range(max_try):
        cur_num = int(input("Enter the number: "))
        if cur_num == num:
            print(f"You win! Attempt - {i + 1}")
            break
        elif num > cur_num:
            print(f"More... Attempt - {i + 1}")
        else:
            print(f"Less... Attempt - {i + 1}")
    if i + 1 == max_try:
        print("All attempts is over. You loose.")


num = random.randint(LOWER_LIMIT, UPPER_LIMIT)
print(f"Secret number - {num}")
guess_number(MAX_TRY)
