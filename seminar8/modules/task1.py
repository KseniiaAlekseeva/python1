import json

with open('../test/file3.txt', 'r', encoding='utf8') as f:
    data = []
    for line in f:
        data.append(line.title())
    data = ''.join(data)

with open('../test/file3.json', 'w', encoding='utf8') as jf:
    json.dump(data, jf, indent=4)
