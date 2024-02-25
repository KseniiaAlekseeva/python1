backpack = {'knife': 0.4,
            'spoon': 0.2,
            'cup': 0.6,
            'fork': 0.1,
            'blanket': 1.5,
            'pillow': 1,
            'air mattress': 2.5,
            'column': 0.8,
            'power bank': 0.5}
max_weight = 4
weight = 0
items = []

for k, v in backpack.items():
    weight += v
    if weight <= max_weight:
        items.append(k)
    else:
        weight -= v
        break
print(f'Weight: {weight}, items: {items}')
