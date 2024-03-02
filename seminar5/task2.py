string = 'Let\'s go! My best friend.'
my_dict = {letter: ord(letter) for letter in string}
print(my_dict)
my_iter = iter(my_dict.items())
for i in range(5):
    print(next(my_iter))
