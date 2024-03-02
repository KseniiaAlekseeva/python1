# Напишите однострочный генератор словаря, который принимает на вход три списка
# одинаковой длины: имена str, ставка int, премия str с указанием процентов вида “10.25%”.
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии

def calc_reward(names: list, salary: list, bonus: list) -> dict:
    return {name: sal * float(percent.strip('%')) / 100 for name, sal, percent in zip(names, salary, bonus)}


if __name__ == '__main__':
    names = ['Katya', 'Vasya', 'Petya']
    salary = [100000, 200000, 115000]
    bonus = ['10%', '22.4%', '10%']
    print(calc_reward(names, salary, bonus))
