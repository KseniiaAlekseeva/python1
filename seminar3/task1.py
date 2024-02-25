my_list = [1, 2, 2, 4, 4, 5]
my_set = set(my_list)
print(my_set)

new_list=[]
for item in my_list:
    if item not in new_list:
        new_list.append(item)
print(my_set)
