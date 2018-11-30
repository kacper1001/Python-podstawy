DATABASE = [
    {'last_name': 'Jiménez'},
    {'first_name': 'Mark', 'last_name': 'Watney'},
    {'first_name': 'Иван', 'age': 42},
    {'first_name': 'Matt', 'last_name': 'Kowalski', 'born': 1961},
    {'first_name': 'José', 'born': 1961, 'agency': 'NASA'},
]
cos =list()
keys = []
for row in DATABASE:
    cos.append({value: keys for keys, value in row.items()})

print(cos)
