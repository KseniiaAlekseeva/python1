import random as rnd

_dict_riddles = {}

__all__ = ['start_riddles']


def list_riddles():
    my_dict = {'Who is black?': ['cat', 'dog', 'snake'],
               'Who is white?': ['bird', 'sky', 'paper'],
               'Who is orange?': ['orange', 'apple', 'candy']}
    for k, v in my_dict.items():
        attempt = guess_riddle(k, v, 3)
        yield k, attempt
        print(attempt)


def make_guess_dict(rid: str, attempt_num: int):
    if rid not in _dict_riddles:
        _dict_riddles[rid] = []
    _dict_riddles[rid].append(attempt_num)


def riddle_results():
    for v in _dict_riddles.values():
        print(*v)


def start_riddles():
    for i, j in list_riddles():
        make_guess_dict(i, j)
    riddle_results()


def guess_riddle(riddle: str, answers: list, attempts: int) -> int:
    true_answer = rnd.randint(0, len(answers) - 1)
    print('True answer: ', answers[true_answer])
    print(riddle)
    for i, j in enumerate(answers, 1):
        print(f'{i} - {j}')
    count = 0
    while count < attempts:
        count += 1
        cur_answer = int(input('Enter your answer: ')) - 1
        if cur_answer == true_answer:
            print('You win!')
            return count
        else:
            print('Wrong answer...')
    print('You loose!')
    return 0
