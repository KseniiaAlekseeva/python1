my_dict = {'Ira': ['orange', 'tomato', 'apple'],
           'Vanya': ['tomato', 'coconut'],
           'Petya': ['tomato', 'apple', 'kiwi']}
my_set = set(list(my_dict.values())[0])
for item in my_dict.values():
    my_set = my_set.intersection(set(item))
print(my_set)

new_dict = {}
for v in my_dict.values():
    for item in v:
        if item not in new_dict:
            new_dict[item] = 0
        new_dict[item] += 1
print(new_dict)

for k, v in new_dict.items():
    if v == 1:
        print('Only one - ', k)

for k, v in new_dict.items():
    if v == 2:
        print('Only two - ', k)
        for key, value in my_dict.items():
            if k not in value:
                print(f'{key} dont have {k}.')
                break
