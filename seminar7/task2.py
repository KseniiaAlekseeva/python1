from random import randint, choice

VOWELS = {'a', 'o', 'u', 'e', 'i', 'y'}


def gen_name(min_len, max_len) -> str:
    """
    Generates random name.
    """
    length = randint(min_len, max_len)
    min_code = ord('a')
    max_code = ord('z')
    name = []
    flag = False
    for _ in range(length):
        letter = chr(randint(min_code, max_code))
        name.append(letter)
        if letter in VOWELS:
            flag = True
    if not flag:
        i = randint(0, len(name) - 1)
        letter = choice(list(VOWELS))
        name[i] = letter
    return ''.join(name).title()


def print_names(num_lines: int, name: str) -> None:
    """
    Writes names to file.
    """
    with open(name, 'a', encoding='utf-8') as f:
        for i in range(num_lines):
            name = gen_name(4, 7)
            f.write(f'{name}\n')


if __name__ == '__main__':
    print_names(5, 'file2.txt')
