import os

__all__ = ['sort_file']
ext_dict = {'video': ['mkv'], 'photo': ['jpeg', 'png'], 'text': ['txt']}


def sort_file(direct: str):
    for file in os.listdir(direct):
        extens = file.split('.')[-1]
        for k, v in ext_dict.items():
            if not os.path.exists(k) or not os.path.isdir(k):
                os.mkdir(k)
            for item in v:
                if extens == item:
                    os.rename(os.path.join(direct, file), os.path.join(k, file))


if __name__ == '__main__':
    sort_file('test_files')
