z = [
    {'id': 1, 'full_name': 'Алекберов Рамиль Русланович'},
    {'id': 2, 'full_name': 'Бобровская Анастасия Дмитриевна'},
    {'id': 3, 'full_name': 'Винговатов Александр Олегович'}
    ]

v = [z['full_name'] for z in z if len(z['full_name'].split())]
print(v)