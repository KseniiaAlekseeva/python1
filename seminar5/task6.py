my_table = (f'{j} * {i} = {j * i}\t' if j < 5 else f'{j} * {i} = {j * i}\n' for i in range(2, 11) for j in range(2, 6))
for i in my_table:
    print(i, end='')
print()
my_table = (f'{j} * {i} = {j * i}\t' if j < 9 else f'{j} * {i} = {j * i}\n' for i in range(2, 11) for j in range(6, 10))
for i in my_table:
    print(i, end='')