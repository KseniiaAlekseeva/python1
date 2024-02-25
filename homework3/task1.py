my_list = [1, 2, '22', 'ds', -18, '22', 2, 0, -18, -18]
dupl_list = []
count = {}
for item in my_list:
    if item not in count:
        count[item] = 0
    count[item] += 1
    if count[item] == 2:
        dupl_list.append(item)
print(count)
print(dupl_list)
