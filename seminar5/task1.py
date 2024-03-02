a, b, c, *d = [int(i) for i in input('Enter numbers, delimited by / :').split('/')]
my_dict = {b: a, c: tuple(d)}
print(my_dict)
