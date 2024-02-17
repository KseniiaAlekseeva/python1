def main():
    balance = 0
    count = 0
    while True:
        while True:
            op = int(input('Enter 1 - add, 2- get, 3 - exit: \n'))
            if op not in (1, 2, 3):
                print('Wrong operation number!')
            else:
                break
        match op:
            case 1:
                balance, count = add_money(balance, count)
                show_balance(balance, count)
            case 2:
                balance, count = get_money(balance, count)
                show_balance(balance, count)
            case 3:
                show_balance(balance, count)
                break


def add_money(balance, count):
    summ = 0

    if balance > 5e6:
        balance *= 0.9

    while True:
        try:
            summ = int(input('Enter sum for adding multiple 50: '))
        except ValueError:
            ex = input('Press 0 to exit: ')
            if ex != '0':
                continue
            else:
                return balance, count
        if summ % 50 == 0:
            count += 1
            break
    balance += summ
    if count % 3 == 0:
        balance *= 1.03
    return balance, count


def get_money(balance, count):
    summ = 0
    commission = 0
    if balance > 5e6:
        balance *= 0.9

    while True:
        try:
            summ = int(input('Enter sum for getting multiple 50: '))
        except ValueError:
            ex = input('Press 0 to exit: ')
            if ex != '0':
                continue
            else:
                return balance, count
        if summ % 50 == 0:
            commission = summ * 0.015
            if commission < 30:
                commission = 30
            elif commission > 600:
                commission = 600
            if summ + commission <= balance:
                count += 1
                break
            else:
                print('Not enough money on balance.')

    balance -= (summ + commission)
    if count % 3 == 0:
        balance *= 1.03
    return balance, count


def show_balance(balance, count):
    print(f'balance = {balance}, count= {count}')


if __name__ == "__main__":
    main()
