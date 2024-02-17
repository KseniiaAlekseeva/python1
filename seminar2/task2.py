BIN = 2
HEX = 8

num = int(input('Enter the number: '))
result = ''

basis = BIN
while num > 0:
    result = str(num % basis) + result
    num = num // basis

print(result)
