import json
import os.path

__all__ = ['read_csv']


def read_csv(csv_name: str, json_name: str) -> None:
    if not os.path.exists(csv_name):
        raise FileNotFoundError('File not found.')
    with open(csv_name, 'r', encoding='utf8') as cf, open(json_name, 'a', encoding='utf8') as jf:
        for line in cf:
            level, ident, name = line.strip().split(',')
            ident = f'{int(ident):010d}'
            name = name.title()
            hash_name = hash(ident + name)
            my_dict = {level: [ident, name, hash_name]}
            print(json.dumps(my_dict), file=jf)


if __name__ == '__main__':
    read_csv('result.csv', 'result2.json')
