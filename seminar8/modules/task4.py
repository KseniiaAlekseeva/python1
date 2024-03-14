import json
import os.path
import pickle

__all__ = ['json_to_pickle']


class NotDirError(Exception):
    def __str__(self):
        return 'No such directory'


def json_to_pickle(direct: str) -> None:
    if not os.path.exists(direct) or not os.path.isdir(direct):
        raise NotDirError
    for file in os.listdir(direct):
        if file.endswith('.json'):
            with open(os.path.join(direct, file), 'r', encoding='utf8') as jf:
                data = json.load(jf)
            with open(os.path.join(direct, file.replace('.json', '.pickle')), 'wb') as pf:
                pickle.dump(data, pf)


if __name__ == '__main__':
    json_to_pickle('test')
