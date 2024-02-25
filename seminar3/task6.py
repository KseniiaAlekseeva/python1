import string

str = 'Enter yor text, please! How are you? Ohh! Good bye!'
out = str.translate(str.maketrans('', '', string.punctuation)).lower()
words = sorted(out.split())
max_len = len(max(words, key=len))
print(words)
print(max_len)

for i, word in enumerate(words, 1):
    print(f'{i:02} {word:>{max_len}}')

