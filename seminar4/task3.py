def make_dict(text: str) -> dict:
    a, b = sorted([int(i) for i in text.split()])
    return {chr(i): i for i in range(a, b + 1)}


print(make_dict('54 67'))
