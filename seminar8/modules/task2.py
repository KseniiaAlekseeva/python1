import json
import os.path

__all__ = ['read_json', 'write_json', 'write_csv']


def read_json() -> dict:
    if os.path.exists('../test/result.json'):
        with open('../test/result.json', 'r', encoding='utf8') as jf:
            access_dict = json.load(jf)
    else:
        access_dict = {'1': {},
                       '2': {},
                       '3': {},
                       '4': {},
                       '5': {},
                       '6': {},
                       '7': {}}
    return access_dict


def add_records(access_dict):
    while True:
        name = input('Enter your name: ')
        while True:
            flag = False
            ident = input('Enter ID: ')
            for k, v in access_dict.items():
                if ident in v.keys():
                    print('This ID just exists.')
                    flag = True
            if not flag:
                break
        while True:
            level = input('Enter access level 1 - 7: ')
            if '0' < level < '8':
                break
        access_dict[level][ident] = name
        ex = input('Exit? y/n ')
        if ex == 'y':
            break


def write_json(access_dict):
    add_records(access_dict)
    with open('../test/result.json', 'w', encoding='utf8') as jf:
        json.dump(access_dict, jf, indent=4, ensure_ascii=False)


def write_csv(access_dict):
    add_records(access_dict)
    with open('../test/result.csv', 'w', encoding='utf8') as cf:
        for k, v in access_dict.items():
            for k2, v2 in v.items():
                cf.write(f'{k},{k2},{v2}\n')


if __name__ == '__main__':
    write_json(read_json())
    write_csv(read_json())
