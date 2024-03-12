from typing import TextIO


def read_line_or_begin(fd: TextIO) -> str:
    text = fd.readline()
    if text == '':
        fd.seek(0)
        text = fd.readline()
    return text[:-1]


def read_files(name1: str, name2: str, name3: str):
    with open(name1, 'r', encoding='utf8') as f1, \
            open(name2, 'r', encoding='utf8') as f2, \
            open(name3, 'a', encoding='utf8') as f3:
        length = max(len(f1.readlines()), len(f2.readlines()))
        for _ in range(length):
            line1 = read_line_or_begin(f1)
            line2 = read_line_or_begin(f2)
            a, b = [float(i) for i in line1.split(' | ')]
            res = a * b
            if res > 0:
                name = line2.upper()
                res = round(res)
            else:
                name = line2.lower()
                res = abs(res)
            f3.write(f'{name} {res}\n')


if __name__ == '__main__':
    read_files('file1.txt', 'file2.txt', 'file3.txt')
