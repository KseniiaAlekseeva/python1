my_list = [3, 5, 7, 2, 9, 2, 7, 5, 5, 2, 8]

new_list = [i for i, j in enumerate(my_list, 1) if j % 2 != 0]
print(new_list)

for item in enumerate(my_list,1):
    print(type(item))