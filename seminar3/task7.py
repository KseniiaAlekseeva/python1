from collections import Counter

str = 'Enter yor text'
print(Counter(str))

my_dict={}
for s in str:
    my_dict[s]=str.count(s)
print(my_dict)