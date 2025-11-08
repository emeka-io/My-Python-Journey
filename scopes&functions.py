#  Scopes in Python
# The scope of a name is the part of a code where the name is properly recognizable.
def number():
    print(f'{numb} is a number')

numb = 37
number()
print(numb)
numb = 10 # this is where the scope of the function ends
number()
print(numb)

#Functions and scopes:
# the global keyword
def number():
    global numb
    numb = 388
    print(f'{numb} is a number')


number()
print(numb)
numb = 27
number()
print(numb)
# numb remains the preassigned value

# WITH THE GLOBAL KEYWORD ; YOU CAN CALL A VARIABLE DEFINED IN A FUNCTION
# OUTSIDE THE FUNCTION

var = 2
print(var)    # outputs: 2

def return_var():
    global var
    var = 5
    return var

print(return_var())    # outputs: 5
print(var)    # outputs: 5

#  How the function interacts with its arguments
def sum_func(x):
    print(f'You entered: {x}')
    x += 1
    print(f'We returned {x}')

num = 2
sum_func(num)
print(num)

a = 1

def fun():
    global a
    a = 2
    print(a)

fun()
a = 3
print(a)
# this prints 3, bcos it was assignes after calling the function

# Creating multi-parameter functions
# Sample functions: Evaluating the BMI ( Body Mass Index)
# BMI = weight/height^2
def ft_and_inch_to_m(ft, inch = 0.0):
    return ft * 0.3048 + inch * 0.0254


def lb_to_kg(lb):
    return lb * 0.4535923


def bmi(weight, height):
    if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
        return None

    return weight / height ** 2


print(bmi(weight = lb_to_kg(176), height = ft_and_inch_to_m(5, 7)))


# Sample functions: Triangles
# program to check if 3 lengths can form a triangle
def is_a_tri(a, b, c):
    if a + b <= c:
        return False
    elif a + c <= b:
        return False
    elif b + c <= a:
        return False
    else:
        return True
    
print(is_a_tri(3, 4, 9))
print(is_a_tri(2,3,4))

# shorter version
def is_a_tri(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return False
    return True
    
a = float(input('Enter the length of the first side: '))
b = float(input('Enter the length of the second side: '))
c = float(input('Enter the length of the third side: '))

if is_a_tri(a, b, c):
    print('YES, your values can build a triangle.')
else:
    print("NO, your values can't build a triangle.")

# adding pythagoras
def is_a_right_ang(a, b, c):
    if not is_a_tri(a, b, c):
        return False
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2
    if b > a and b > c:
        return b ** 2 == a ** 2 + c ** 2
    if c > b and c > a:
        return c ** 2 == a ** 2 + b ** 2
    

print(is_a_right_ang(5, 3, 4))
print(is_a_right_ang(1, 3, 4))


# Evaluating a triangle's area - using Heron's formula 
def is_a_tri(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return False
    return True

def heron(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5 

def area(a, b, c):
    if not is_a_tri(a, b, c):
        return None
    return heron(a, b, c)

print(area(1., 1., 2. ** .5))


# Sample functions: Factorials
def factorials(x):
    if x < 0:
        return None
    if x < 2:
        return 1
    product = 1
    for n in range(2, x + 1):
        product *= n
    return product

for y in range (1, 6):
    print(y, factorials(y)) # prints factorials from 1 - 5


# Fibonacci numbers
# in a fibonacci sequence: 1st elem = 1, Fib2 = 1, Fibi = Fibi-1 + Fibi-2

def fib(x):
    if x < 1:
        return None
    if x < 3:
        return 1
    elem_1 = elem_2 = 1
    the_sum = 0
    for i in range(3, x + 1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum
    return the_sum


for n in range(1, 10):
    print(f'{n} -> {fib(n)}')



#  Recursion - this is when a function calls itself
# using Recursion to make our fib function shorter
def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)

# using Recursion to make our factorials function shorter
def factorials(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * factorials(n - 1)

# but recursive calls consume a lot of memory,
# and therefore may sometimes be inefficient.


