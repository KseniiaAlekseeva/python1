my_gen = (i for i in range(0, 101, 2) if i % 10 + i // 10 != 8)
for i in my_gen:
    print(i, end='\t')
