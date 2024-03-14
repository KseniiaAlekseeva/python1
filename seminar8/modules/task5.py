import pickle

__all__ = ['gen_pickle', 'pickle_to_csv', 'csv_to_print_pickle']

my_dict = [{1: 'mari'},
           {2: 'Karina', 3: 'Inga'},
           {4: 'Lesya'}]


def gen_pickle():
    with open('../test/dict.pickle', 'wb') as pf:
        pickle.dump(my_dict, pf)


def pickle_to_csv():
    with open('../test/dict.pickle', 'rb') as pf:
        data = pickle.load(pf)
    with open('../test/dict.csv', 'w', encoding='utf8') as cf:
        print(f'Column1,Column2', file=cf)
        for dic in my_dict:
            for k, v in dic.items():
                print(f'{k},{v}', file=cf)


def csv_to_print_pickle():
    with open('../test/dict.csv', 'r', encoding='utf8') as cf:
        data = []
        for line in cf:
            k, v = line.strip().split(',')
            data.append({k: v})
    print(pickle.dumps(data))


if __name__ == '__main__':
    # gen_pickle()
    # pickle_to_csv()
    csv_to_print_pickle()
