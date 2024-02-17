import decimal
import math

decimal.getcontext().prec = 50
PI = decimal.Decimal(math.pi)
diam = decimal.Decimal(input('Enter the diameter: '))
print('Square of the cycle: ', PI*(diam/2)**2, 'length of the cycle: ', PI*diam)
