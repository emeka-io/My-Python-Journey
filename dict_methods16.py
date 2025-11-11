# Dictionary methods and functions
users: dict = {0: 'Mario', 1: 'Luigi', 2: 'James'}
# 1. values() - this prints all the values
print(users.values())

# 2. users() - this prints all the keys
print(users.keys())

# 3. pop() - deletes a specified key, it can be assigned it to a variable
popped = users.pop(2)
print(popped)
print(users)

#  4. popitem() - this deletes the last key of our dictionary
users: dict = {0: 'Mario', 1: 'Luigi', 2: 'James'}
users.popitem()
print(users)
users.popitem()
print(users)

# 5. copy()
sample_dict: dict = {0: ['a','b'], 1: ['c', 'd']}
my_copy: dict = sample_dict.copy()
print(my_copy)
print(sample_dict)

print(id(my_copy))
print(id(sample_dict)) # this shows they have diff storage locations

my_copy[0][0] = 'tet'
print(my_copy)
print(sample_dict)

# 6. get()
users: dict = {0: 'Mario', 1: 'Luigi', 2: 'James'}
print(users.get(2))
print(users.get(83))
print(users.get(83, 'missing'))

# 7. setdefault()
users: dict = {0: 'Mario', 1: 'Luigi', 2: 'James'}
print(users.setdefault(0, '???'))
print(users.setdefault(892, '???'))
print(users) # note: 892 has been added


# 8. clear()
users: dict = {0: 'Mario', 1: 'Luigi', 2: 'James'}
users.clear
print(users) # this prints an empty dictionary

# 9. fromkeys()
people: list[str] = ['Mario', 'Luigi', 'James']
users: dict = dict.fromkeys(people)
print(users) # this gives a value of None to all

users: dict = dict.fromkeys(people, 'Person')
print(users)

# 10. items()
users: dict = {0: 'Mario', 1: 'Luigi', 2: 'James'}
print(users.items())

for k, v in users.items():
    print(k,v)

# 11. update()
users: dict = {0: 'Mario', 1: 'Luigi', 2: 'James'}
users.update({11: 'ali', 2: 'rice'})
print(users) # rice overwrites james
# THIS METHOD IS OLD 
# USING THE UNION OPERATOR
print(users | {11: 'ali', 2: 'rice'})
users |= {11: 'ali', 2: 'rice'}
print(users)