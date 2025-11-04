# PYTHON REVISION WITH GEEKSFORGEEKS
# input and output in python
# INPUT
name = input("Whats your name: ")
print(f"Hello, {name}")

# Printing Variables
s = 'say'
j = 'bake'
k = 'call'
print(s, j, k) # this prints all the variables in one line

# Taking Multiple Input in Python
# takimg 2 inputs using 'split()'
x, y = input('Enter two numbers: ').split()
print(f'Number of tables: {x}')
print(f'Number of chairs: {y}')

# takimg 3 inputs using 'split()'
a, b, c = input("Enter three numbers: ").split()
print(f'Numbers of books: {a}')
print(f'Number of pens: {b}')
print(f"Number of Pencils: {c}")

# Finding DataType of Input in Python
print(type(a))
print(type(name))

# Python Variables
# assigning values
a = 'apple'
b = 25
#Assigning the Same Value to multiple variables
r = e = d = j = 50
#Assigning the Different Value to multiple variables
r, e, d, j = 3, 5, 'life', 8.05

# Type Casting a Variable
# using int()
num = 56.05
print(int(num)) # this converts it to an integer
# using float()
numb = 67 
print(float(numb))
# using str()
number = 43
print(str(number))

# Object Reference in Python
j = 5
k = j
j = 20
print(j, k) # note that k still = 5

# Delete a Variable Using del Keyword
i = 50 
del i # this deletes i from the program

# Swapping Two Variables
d = 10
w = 40
d, w = w, d
print (d, w)

# Counting Characters in a String
name = 'EMEKA'
length = len(name)
print(f'Length of the word: {length}')

# Python Data Types
# examples of data types in python
x = 20 # int
x = 90.33 # float
x = ' hello ' # string
print(x[1]) # prints the 2nd item in the string
x = ['hello', 'python', 'code'] # list
x = ('hello', 'python', 'code') # tuple
# LISTS
a = [1, 3, 5, 7]
b = ['python', 'code', 'program']
print(a)
# Accessing List Items
print(a[0]) #prints first item
print(a[-1]) # prints last item
print(b[1])

#Tuple Data Type
# unlike lists, tuples cannot be modified after creation.
c = ('this', 'is', 'a', 'tuple') # with parentheses
d = 'this', 'is', 'also', 'a', 'tuple' # without parentheses

#Accessing Tuple Items
# this is similar to that of lists.
print(c[1])
print(d[-2])

#  Boolean Data Type
# these are True and False - NOTE: they are  case sensitive
print(type(True))
print(type(False))

# Set Data Type
# Set is an unordered collection of data types that is iterable, mutable, and has no duplicate elements.
# a set cannot contain duplicates.
e = set(['this', 'is', 'a', 'set'])
f = set('THIS IS ALSO A SET')
set1 = set(["Geeks", "For", "Geeks"]) #Duplicates are removed automatically
print(set1) 
# loop through set
for i in set1:
   print(i, end=" ") #prints elements one by one
  
# check if item exist in set   
print("Geeks" in set1)

# Dictionary Data Type
g = {1: 'this', 2: 'is', 3: 'a', 4: 'dictionary'}
print(g)

g_dict = dict(g)
print(g_dict)

# Accessing Key-value in Dictionary
print(g[3])

print(g.get(4))

# Truthy vs Falsy Values in Python
number = 7
if number:
   print("7 IS TRUTHY")

number = 0
if number:
   print("0 IS TRUTHY")  # this does not print beacuse its false

# Truthy Values
# Non-empty sequences or collections: [ 1 ], ( 0, ), "Hello", { 1:2 }
# Numeric values not equal to zero: 1, -4, 3.5
# Constant: True - all these are truthy values
if [1,3,4]:
   print("THIS IS TRUTHY")

if -329:
   print("THIS IS TRUTHY")

# Falsy Values
# Empty sequences and collections: [ ], ( ), { }, set( ), " ", range(0)
# Numbers: 0 (integer), 0.0 (float), 0j (complex)
# Constants: None, False - all these are falsy

if 0:
   print('This is truthy')

if ( ):
   print('This is truthy')

#NOTE that nothing prints

# USING TRUTHY & FALSY VALUES TO SOLVE REAL PROBLEMS.
# a program to find odd & even number 
num1 = int(input("Enter a number: "))
if num1 % 2:
   print(f'{num1} is an odd number.')
else:
   print(f'{num1} is an even number.')


num2 = int(input("Enter a number: "))
if num2 % 2:
   print(f'{num2} is an odd number.')
else:
   print(f'{num2} is an even number.')


# using the Built-in bool() function
print(bool(7)) # truthy
print(bool(0)) # falsy