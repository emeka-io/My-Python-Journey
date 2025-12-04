# REVISION OF DICTIONARIES IN PYTHON
capitals = {"USA" : "Washington",
            'India' : 'New Delhi',
            'China' : 'Beijing',
            'Russia' : 'Moscow'}

# to see all the methods of a dictionary
print(dir(capitals)) # or 
print(help(capitals))

print(capitals.get('USA'))
print(capitals.get('India'))
print(capitals.get('USA'))

if capitals.get('USA'):
    print(f'The capital is {capitals.get('USA')}')
else:
    print('This capital does not exist.')

if capitals.get('Brazil'):
    print(f'The capital is {capitals.get('Brazil')}')
else:
    print('This capital does not exist.')

capitals.update({'Brazil': 'Brasília'})

if capitals.get('Brazil'):
    print(f'The capital is {capitals.get('Brazil')}')
else:
    print('This capital does not exist.')

capitals.update({'USA': 'Texas'})

print(capitals) # washington has been replaced.

keys = capitals.keys()
for key in capitals.keys():
    print(keys) 

values = capitals.values()
for value in capitals.values():
    print(values)


for key, value in capitals.items():
    print(f'{key}: {value}')