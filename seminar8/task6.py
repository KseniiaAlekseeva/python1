import os
import json
import csv
import pickle

# my_dict={root1:[(name,parent,type,size),(name,parent,type,size)],
#          root2:[(name,parent,type,size)]}

my_dict = {}


def read_directory(direct):
    for root, dirs, files in os.walk(direct):
        print(root, dirs, files)
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
            my_dict[root].append((name, parent, typ, size))

def write_json_csv_pickle(my_dict):

def write_json_csv_pickle(directory):
    # write_JSON
    result_dict_json = {}
    for dir_path, dir_file, file_name in os.walk(directory):
        result_dict_json[f'DIRECTORY - {dir_path}'] = [
            f'FILE - {i} = {os.path.getsize(os.path.abspath(dir_path + "/" + i))} byte' for i in file_name]
    with open('json_file.json', 'w', encoding='utf-8') as json_file:
        json.dump(result_dict_json, json_file, indent=4, separators=(',', ':'))
    # write_CSV
    data = [["Dir", "Files"]]
    for key, value in result_dict_json.items():
        data.append([key, value])
    with open('csv_file.csv', 'w', encoding='utf-8') as csv_f:
        write_csv = csv.writer(csv_f, dialect='excel-tab', delimiter=',')
        write_csv.writerows(data)
    # write PICKLE
    with open('pickle_file.bin', 'wb') as pickle_file:
        pickle.dump(result_dict_json, pickle_file)


if __name__ == '__main__':
    # write_json_csv_pickle('testdir')
    read_directory('testdir')
    print(my_dict)
