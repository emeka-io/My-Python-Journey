# Section 6 – Tuples and dictionaries
# 4.6.1 Sequence types and mutability
# a sequence is data which can be scanned by the for loop.
#  mutability − is a property of any Python data that describes its 
# - readiness to be freely changed during program execution.

# Tuples - an immutable sequence type
# a tuples is usally written in parentheses, but it can also be written without it
tuple_1 = (1, 2, 4, 8)
tuple_2 = 1., .5, .25, .125
# both are tuples
print(tuple_1)
print(tuple_2)

# while creating a one-elemaent tuple, you end it with a comma for it to be distinguishable
one_elem_tup = (2, )
print(one_elem_tup)

# How to use a tuple
my_tuple = (1, 10, 100, 1000)

print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:])
print(my_tuple[:-2])

for elem in my_tuple:
    print(elem)

# note: tuples are not editable, no append,  no insert
# however the following also work on tuples
my_tuple = (1, 10, 100)

t1 = my_tuple + (1000, 10000)
t2 = my_tuple * 3

print(len(t2))
print(t1)
print(t2)
print(10 in my_tuple)
print(-10 not in my_tuple)

# more of tuples
var = 123

t1 = (1, )
t2 = (2, )
t3 = (3, var)

t1, t2, t3 = t2, t3, t1

print(t1, t2, t3)

# Dictionaries
# a dictionary as the name implies is a data type in python whereby
# the word you look for is named a key.
# The word you get from the dictionary is called a value.
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
phone_numbers = {'boss': 5551234567, 'Suzy': 22657854310}
empty_dictionary = {}

print(dictionary)
print(phone_numbers)
print(empty_dictionary)
# printing parts of a list
print(dictionary['cat'])
print(phone_numbers['Suzy'])

# checking if a word is in a list
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
words = ['cat', 'lion', 'horse']
for i in words:
    if i in dictionary:
        print(f'{i} -> {dictionary[i]}')
    else:
        print(f"{i} is not in dictionary. ")

# WRITING LISTS WITH HANGING INDENT
# Example 1:
dictionary = {
              "cat": "chat",
              "dog": "chien",
              "horse": "cheval"
}
# Example 2:
phone_numbers = {'boss': 5551234567,
              'Suzy': 22657854310
}

