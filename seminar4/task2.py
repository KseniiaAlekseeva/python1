def sort_codes(text: str) -> list:
    return sorted(set([ord(c) for c in text]), reverse=True)


text = 'Enter yor text, please! How are you? Ohh! Good bye!'
print(sort_codes(text))
