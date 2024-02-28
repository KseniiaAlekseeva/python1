import string


def print_words(text: str) -> None:
    out = text.translate(str.maketrans('', '', string.punctuation)).lower()
    words = sorted(out.split())
    max_len = len(max(words, key=len))
    print(words)
    print(max_len)

    for i, word in enumerate(words, 1):
        print(f'{i:02} {word:>{max_len}}')


text = 'Enter yor text, please! How are you? Ohh! Good bye!'
print_words(text)
