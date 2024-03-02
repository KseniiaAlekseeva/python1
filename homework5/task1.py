import os
import sys


def get_dir_name_ext(path: str) -> tuple:
    dir, (name, ext) = (os.path.splitext(i) if '.' in i else i for i in os.path.split(path))
    return dir, name, ext


# res = [(x, y, z) for x, (y, z) in test_list]

if __name__ == '__main__':
    path = os.path.realpath(sys.argv[0])
    print(path)
    print(get_dir_name_ext(path))

