from datetime import date


def menu() -> None:
    balance = 0
    count = 0
    ops_log = []

    while True:
        while True:
            op = int(input('Enter 1 - add, 2 - get, 3 - show operations log, 4 - exit: \n'))
            if op not in (1, 2, 3, 4):
                print('Wrong operation number!')
                ops_log.append(f'{date.today()}: Entered wrong operation.')
            else:
                break
        match op:
            case 1:
                balance, count = add_money(balance, count, ops_log)
                show_balance(balance, count)
            case 2:
                balance, count = get_money(balance, count, ops_log)
                show_balance(balance, count)
            case 3:
                print_log(ops_log)
            case 4:
                show_balance(balance, count)
                break


def add_money(balance: float, count: int, ops_log: list) -> (float, int):
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
    message = str(date.today()) + ' Added ' + str(summ)
    if count % 3 == 0:
        balance *= 1.03
        message += '. Added 3 % for 3d operation'
    message += '. Balance ' + str(balance) + '.'
    ops_log.append(message)
    return balance, count


def get_money(balance: float, count: int, ops_log: list) -> (float, int):
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
    message = str(date.today()) + ' Got ' + str(summ) + '. Commission ' + str(commission)
    if count % 3 == 0:
        balance *= 1.03
        message += '. Added 3 % for 3d operation'
    message += '. Balance ' + str(balance) + '.'
    ops_log.append(message)
    return balance, count


def show_balance(balance: float, count: int) -> None:
    print(f'balance = {balance}, count= {count}')


def print_log(operations: list) -> None:
    for op in operations:
        print(op)


if __name__ == "__main__":
    menu()
