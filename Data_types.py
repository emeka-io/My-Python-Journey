# WORKING WITH SEVERAL DATA TYPES IN PYTHON
#TUPLES
#THESE ARE NOT EDITABLE
coordinates = (0, 1, 2)
# UNPACKING TUPLES
coordinates = (0, 1, 2)
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]
print(x + y + z)

# OR
x, y, z = coordinates
print(x + y + z)

# DICTIONARIES
student = {
    'name': 'John Adams',
    'Class': 'SS 3',
    'Gender': 'Male'
}

print(student['Gender'])
print(student.get('Class')) # this does not return an error for non existing keys
print(student.get('Date'))
print(student.get('Date', 'Nov 7 2025')) # to assign a value

digits = {
    '1' : 'One',
    '2' : 'Two',
    '3' : 'Three',
    '4' : 'Four',
    '5' : 'Five'
}

phone = input('Enter your phone number: ')
for i in phone:
    print(digits[i], end= ' ')



# EXCEPTIONS - ERROR
try:
    age = int(input('Enter your age: '))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print('Age cannot be 0.')
except ValueError:
    print('Invalid Input')

# CLASSES
# using pascal naming convention, we start each new word in our class name with a capital letter
class Point:
    def move(self):
        print('move')
    
    def draw(self):
        print('draw')

point1 = Point()
point1.x = 10
print(point1.x)
point1.draw()

point2 = Point()
point2.x =90

# CONSTUCTORS
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def move(self):
        print('move')
    
    def draw(self):
        print('draw')


point = Point(10, 30)
print(point.y)

class Person:
    def __init__(self, name):
        self.name = name
        
    def talk(self):
        print(f"Hi, I am {self.name}")

John = Person('John')
John.talk()

Bob = Person('Bob Smith')
Bob.talk()

# INHERITANCE
# thuis is aan initial class
class Dog:
    def walk(self):
        print("Walk")

# lets try repeating it here in another calss
class Cat:
    def walk(self):
        print('Walk') # this method causes repition, which isnt good

# lets fix it by creating a parent class
class Parent:
    def walk(self):
        print("Walk")


class Dog(Parent): # thats all
    pass # to ommit this child class

class Cat(Parent):
    def meow(self):
        print('Meow') # this adds methods specific to this class only.

# now our code is sherter and easily editable
dog1 = Dog()
dog1.walk()
cat1 = Cat()
cat1.meow()
