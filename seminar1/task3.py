import random

LOWER_LIMIT = 0
UPPER_LIMIT = 50
MAX_TRY = 10


def guess_number(max_try):
    count = 0
    while count < max_try:
        count += 1
        cur_num = int(input("Enter the number: "))
        if cur_num == num:
            print(f"You win! Attempt - {count}")
            break
        elif num > cur_num:
            print(f"More... Attempt - {count}")
        else:
            print(f"Less... Attempt - {count}")
    if count == max_try:
        print("All attempts is over. You loose.")


num = random.randint(LOWER_LIMIT, UPPER_LIMIT)
print(f"Secret number - {num}")
guess_number(MAX_TRY)
