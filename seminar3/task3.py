my_tuple = (1, [2, 2], 3, 'ygj', 1, 'ttt', [5, 'rr', 'yy'])
my_dict = {}

for item in my_tuple:
    curr_type = type(item).__name__
    if curr_type not in my_dict:
        my_dict[curr_type] = []
    my_dict[curr_type].append(item)

print(my_dict)
