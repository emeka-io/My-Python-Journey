# SOLVING PROBLEMS USING OPERATORS IN PYTHON
# if Statement (CONDITIONAL STATEMENT)
# Problem 1: Check if user is eligible to vote
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")

# Problem 2: Check if a number is positive
num = int(input("Enter a number: "))
if num > 0:
    print("The number is positive.")

# if-else Statement
# Problem 1: Check if a student is pass/fail in exam.
marks = int(input("Enter your marks: "))

if marks >= 50:
    print("You passed the exam.")
else:
    print("You failed the exam.")

# Problem 2: Check if a user has balance to buy an item
balance = float(input("Enter your balance: "))
price = float(input("Enter the item price: "))

if balance >= price:
    print("Purchase successful.")
else:
    print("Insufficient funds.")

# if-elif-else Statement
# Problem 1: Suggest a mode of transport based on distance
distance = float(input("Enter the distance to your destination (in km): "))

if distance <= 2:
    print("You can walk.")
elif distance <= 10:
    print("Use a bicycle or scooter.")
elif distance <= 50:
    print("Take a car or public transport.")
else:
    print("Consider a train or flight.")

# Problem 2: Battery status
battery = int(input("Enter battery percentage: "))

if battery > 80:
    print("Battery Well Charged")
elif battery > 49:
    print("Battery Half")
else:
    print("Battery Low")

# Nested if-else Statement
# Problem 1: Login with username and password
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin":
    if password == "1234":
        print("Access granted")
    else:
        print("Incorrect password")
else:
    print("Username not found")

# Problem 2: Check exam pass and scholarship eligibility
marks = int(input("Enter your Score: "))

if marks >= 50:
    if marks >= 80:
        print("Passed with scholarship")
    else:
        print("Passed without scholarship")
else:
    print("Failed")

# Ternary Statement
# Problem 1: Check if number is even
num = int(input("Enter a number: "))
print("Even" if num % 2 == 0 else "Odd")


# Problem 2: Compare two numbers
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

print("a is greater" if a > b else "b is greater")

# Problem 3: Temperature check
temp = int(input("Enter the temperature: "))
print("Hot" if temp > 25 else "Cool")

# Match- case Statement
# Problem 1: Assign grade
grade = input("Enter your grade (A/B/C): ").upper()

match grade:
    case "A":
        print("Excellent")
    case "B":
        print("Good")
    case "C":
        print("Average")
    case _:
        print("Fail")

# Problem 2: Activity Suggestion based on weather condition
weather = input("Enter the weather (sunny/rainy/cloudy/snowy): ").lower()

match weather:
    case "sunny":
        print("Great day for a picnic!")
    case "rainy":
        print("Stay indoors and read a book.")
    case "cloudy":
        print("Perfect time for a walk.")
    case "snowy":
        print("Build a snowman or go skiing!")
    case _:
        print("Unknown weather condition.")

# Problem 3: Mobile notification settings based on user profile mode
mode = input("Enter phone mode (silent/vibrate/loud/do not disturb): ").lower()

match mode:
    case "silent":
        print("Notifications are muted.")
    case "vibrate":
        print("Phone will vibrate for notifications.")
    case "loud":
        print("All notifications will play sound.")
    case "do not disturb":
        print("No calls or notifications will come through.")
    case _:
        print("Invalid mode selected.")