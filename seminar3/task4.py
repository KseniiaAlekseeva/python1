from collections import Counter

my_list = [3, 5, 3, 5, 5, 7, 7, 8, 10]
count = {}

for item in my_list:
    if item not in count:
        count[item] = 0
    count[item] += 1
print(count)

count2 = Counter(my_list)
print(count2)

for k, v in count2.items():
    if v == 2:
        my_list.remove(k)
        my_list.remove(k)

print(my_list)
