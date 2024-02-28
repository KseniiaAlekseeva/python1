import typing


def reverse_dict(**data) -> dict:
    result = {}
    print(data)
    for k, v in data.items():
        if not isinstance(v, typing.Hashable):
            v = str(v)
        result[v] = k
    return result


if __name__ == '__main__':
    print(reverse_dict(firstname="Sita",
                       age=22,
                       weight=22,
                       temperature=[3.2, 2.4],
                       fruits={'orange': 2.4, 'apple': 1.9}))
