import os

__all__ = ['group_rename']


def group_rename(direct: str,
                 init_ext: str,
                 final_ext: str,
                 name: str = '',
                 saved_name: tuple = (0, 0),
                 num_dig: int = 4):
    count = 0
    for file in os.listdir(direct):
        extens = os.path.splitext(file)[-1]
        if extens == init_ext:
            count += 1
            min_save = saved_name[0]
            max_save = saved_name[1] + 1
            template = '{:0' + str(num_dig) + '}'
            new_name = file[min_save:max_save] + '_' + name + '_' + template.format(count) + final_ext
            os.rename(os.path.join(direct, file), os.path.join(direct, new_name))


if __name__ == '__main__':
    group_rename('test_files', '.txt', '.csv', 'new', (1, 3), 3)
