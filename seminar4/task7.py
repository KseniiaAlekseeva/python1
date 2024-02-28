def calc_income(finances: dict) -> bool:
    print([sum(v) for v in finances.values()])
    return all([sum(v) > 0 for v in finances.values()])


if __name__ == '__main__':
    finances = {'GHP': [12000, -3000, 2000, -12000, 9000],
                'IOP': [2000, -10000, 9000],
                'IUY': [12000, -3000]}
    print(calc_income(finances))
