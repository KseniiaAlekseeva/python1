import fractions


def main():
    print('First fraction:')
    a, b = enter_fraction()
    print('Second fraction:')
    c, d = enter_fraction()
    print('Correct sum: ', fractions.Fraction(a, b) + fractions.Fraction(c, d))
    print('Correct multi: ', fractions.Fraction(a, b) * fractions.Fraction(c, d))
    e, f = fraction_sum(a, b, c, d)
    print(f'Sum: {e}/{f}')
    e, f = fraction_multi(a, b, c, d)
    print(f'Multi: {e}/{f}')


def enter_fraction():
    a, b = 0, 0
    while True:
        fraction = input('Enter the fraction a/b: ')
        try:
            a, b = map(int, fraction.split('/'))
        except ValueError:
            print('wrong format...')
            continue
        if int(b) != 0:
            print('ok...')
            break
        else:
            print('b cant be zero...')
    return a, b


def fraction_sum(a, b, c, d):
    e = a * d + b * c
    f = b * d
    return simplify(e, f)


def fraction_multi(a, b, c, d):
    e = a * c
    f = b * d
    return simplify(e, f)


def simplify(a, b):
    gc = gcd(a, b)
    a //= gc
    b //= gc
    return a, b


def gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return a or b


if __name__ == "__main__":
    main()
