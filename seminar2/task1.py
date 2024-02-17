import sys
import typing

a: int = 3
b: str = 'Hello'
c: float = 3.14
d: tuple = (8, 4, 'a')

e: list = [8, 4, 'a']
f: dict = {'a': 1, 'b': 2, 'c': 3}
g: set = {7, 'a', 3.14}
h: set = {7, d}
# i: set2 = {e, f, g}

data = [a, b, c, d, e, a, f, d, g]

for i, value in enumerate(data):
    print(i + 1,
          value,
          id(value),
          sys.getsizeof(value),
          hash(value) if isinstance(value, typing.Hashable) else 'NoHash',
          'Integer' if isinstance(value, int) else 'NotInteger')
