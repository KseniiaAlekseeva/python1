def rename_variables(symbols: str) -> None:
    new_variables = {}
    for name in globals().keys():
        if name.endswith(symbols) and name != symbols:
            new_variables[name.strip(symbols)] = globals()[name]
            globals()[name] = None
    for k, v in new_variables.items():
        globals()[k] = v


if __name__ == '__main__':
    items = 324
    s = 3
    print(globals())
    rename_variables('s')
    print(globals())
