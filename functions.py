# 4.1 Section 1 – Functions
# A function is a block of code that performs a specific task
# when the function is called (invoked). 

# My first function
def message():
    print("Enter a value: ")

message()
a = int(input())
message()
b = int(input())
message()
c = int(input())

#  a function which doesn't take any arguments,
def message():
    print('Hello, there.')

message()

# a function which takes arguments
def welcome(name):
    print(f'Hello, {name}.')

name = input("What's your name? ")
welcome(name)

# Section 2 –
# How functions communicate with their environment
# Parameterized functions 
# A parameter is actually a variable that exists only 
# inside functions in which they have been defined
def message(x):
    print(f'Enter a number: {x}')

message(5)

# it's possible, to have a variable named the same as a function's parameter.
def message(x):
    print(f'Your number is: {x}')

x = 333
message(3) # this runs the function
print(x) # this prints '333'

# A situation like this activates a mechanism called shadowing

# function with two parameters
def shop(a, b):
    print(f"You're buying a '{a}' for '${b}'")

shop('book', 10)

# Positional parameter passing
# this is a technique which assigns the ith argument to the ith function parameter
def name(first_name, last_name):
    print(f'Your name is: {first_name} {last_name}')

name('Alisson', 'Becker' )

# Keyword argument passing
# here the argument is dictated by its name, not by its position 
def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)

introduction(first_name = "James", last_name = "Bond")
introduction(last_name = "Skywalker", first_name = "Luke")

# Mixing positional and keyword arguments
# positional arguments always come before keyword arguments.
def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)

adding(2, 4, 3)

adding(2, c = 5, b = 9) # this is also correct

# Parametrized functions – more details
# setting a fixed value in the function
def intro(first_name, last_name = 'AYO'):
    print(f'Hello, my name is {first_name}, {last_name}')

intro('rio', 'jane') # this returns both arguments
intro('rio') # this uses the default last_name

# setting a value for both parameters
def introduction(first_name="John", last_name="Smith"):
    print("Hello, my name is", first_name, last_name)

introduction()
introduction(last_name="Hopkins")

# 3 parameter function
def address(street, city, postal_code):
    print("Your address is:", street, "St.,", city, postal_code)

s = input("Street: ")
p_c = input("Postal Code: ")
c = input("City: ")
address(s, c, p_c)


# Section 3 – Returning a result from a function
# Effects and results: the return instruction
# The return instruction has two different variants
# return without an expression
def happy_new_year(wishes = True):
    print("Three...")
    print("Two..")
    print("One.")
    if not wishes:
        return

    print("Happy New Year!")

# testing with no arguments
happy_new_year() # thus assumes true, and runs till the end
happy_new_year(False) # this skips the wish

# return with an expression
# this skips the function and executes its expression
def boring_function():
    return 123

x = boring_function()

print("The boring_function has returned its result. It's:", x)

# the None keyword
value = None
if value is None:
    print("Sorry, you don't carry any value")

# in a function
def strange_function(n):
    if(n % 2 == 0):
        return True

print(strange_function(4))


#  Effects and results: lists and functions
# sending a list as an argument
def list_sum(x):
    s = 0
    for elem in x:
        s += elem
    
    return s 

print(list_sum([2, 4, 9, 4]))

# list as a function result
def list_func(x):
    our_list = [ ]
    for elem in range(x):
        our_list.insert(0, elem)
    return our_list

print(list_func(3))

# A leap year: writing your own functions
def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False
    # Write your code here.
    #


test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr,"->",end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")