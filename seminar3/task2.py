str = input('Enter yor string: ')

if str.isdecimal():
    print(f'This is integer: {int(str)}.')
else:
    try:
        print(f'This is float: {float(str)}.')
    except:
        if str.lower() != str:
            print(f'This is string: {str.lower()}.')
        else:
            print(f'This is string: {str.upper()}.')
