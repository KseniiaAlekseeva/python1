import os
import json
import pickle

__all__ = ['read_directory', 'write_json_csv_pickle']


def read_directory(direct: str) -> dict:
    my_dict = {}
    for root, dirs, files in os.walk(direct):
        for el in dirs + files:
            name = str(el)
            parent = root.split('/')[-1]
            if el in dirs:
                typ = 'DIRECTORY'
                size = 0
                for i in os.listdir(os.path.join(root, name)):
                    if not os.path.isdir(os.path.join(root, el, i)):
                        size += os.path.getsize(os.path.join(root, el, i))
            else:
                typ = 'FILE'
                size = os.path.getsize(os.path.join(root, name))
            if root not in my_dict:
                my_dict[root] = []
            my_dict[root].append({'name': name, 'parent': parent, 'type': typ, 'size': size})
    return my_dict


def write_json_csv_pickle(my_dict: dict) -> None:
    with open('../res.json', 'w', encoding='utf8') as jf:
        json.dump(my_dict, jf, indent=4)
    with open('../res.csv', 'w', encoding='utf8') as cf:
        cf.write('ROOT,NAME,PARENT,TYPE,SIZE\n')
        for k, v in my_dict.items():
            for ele in v:
                cf.write(f'{k},{','.join([str(v2) for v2 in ele.values()])}\n')
    with open('../res.pickle', 'wb') as pf:
        pickle.dump(my_dict, pf)


if __name__ == '__main__':
    write_json_csv_pickle(read_directory('testdir'))
