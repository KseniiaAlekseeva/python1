import os.path
import random

__all__ = ['gen_files', 'gen_files_from_dict']


def gen_str(num_symbols: int) -> str:
    symbols = []
    for _ in range(num_symbols):
        symbols.append(chr(random.randint(ord('a'), ord('z'))))
    return ''.join(symbols)


def gen_files(ext: str, direct: str, min_name: int = 6, max_name: int = 30,
              min_bytes: int = 256, max_bytes: int = 4096, num_files: int = 42):
    if not os.path.exists(direct) or not os.path.isdir(direct):
        os.mkdir(direct)
    for _ in range(num_files):
        while True:
            name = gen_str(random.randint(min_name, max_name))
            if not name + ext in os.listdir(direct):
                break
        bytes = gen_str(random.randint(min_bytes, max_bytes))
        with open(direct + '/' + name + ext, 'w', encoding='utf8') as f:
            f.write(bytes)


def gen_files_from_dict(extensions: dict, dir_name: str):
    for k, v in extensions.items():
        gen_files(ext=k, direct=dir_name, num_files=v)


if __name__ == '__main__':
    # my_dict = {'.jpeg': 1, '.png': 2, '.txt': 3}
    my_dict = {'.txt': 8}
    gen_files_from_dict(my_dict, '../test_files')
