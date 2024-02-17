BIN = 2
OCT = 8
HEX = 16


def main():
    basis = HEX
    letters = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
    num = int(input('Enter the number: '))
    result = ''
    print('Correct number:', hex(num))

    while num > 0:
        div = num % basis
        if div in letters:
            curr = letters[div]
        else:
            curr = str(div)
        result = curr + result
        num = num // basis

    print(result)


if __name__ == "__main__":
    main()
