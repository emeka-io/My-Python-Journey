# Practice Problems using Loops in Python
# for loops
# Problem 1: Print each item in a shopping list
items = input("Enter shopping items separated by commas: ").split(',')

for item in items:
    print("Buy:", item.strip()) # the strip() lists them well

# Problem 2: Print squares of numbers from 1 to n
n = int(input("Enter a number: "))

for i in range(1, n + 1):
    print("Square of", i,"is", i**2)

# while loop
# Problem 1: Countdown timer
seconds = int(input("Enter countdown time in seconds: "))

while seconds > 0:
    print("Time left:", seconds)
    seconds -= 1

# Problem 2: Sum until user enters 0
total = 0
num = int(input("Enter number (0 to stop): "))
while num != 0:
    total += num
    num = int(input("Enter number (0 to stop): "))
print("Total sum:", total)

# Nested for Loops
# Problem 1: Print a multiplication table
n = int(input('ENTER A NUMBER: '))
for i in range(1, n + 1):
    for j in range(1, 11):
        print(i * j, end=' ')
    print()

# Problem 2: Print Identity Matrix Pattern
n = 4

for i in range(n):
    for j in range(n):
        if i == j:
            print("1", end=" ")
        else:
            print("0", end=" ")
    print()  # move to the next row

# Control Flow Statements in Loops
# 1. break
# Problem 1: Stop printing at a target item
items = ["apple", "banana", "cherry", "stop", "mango"]

for item in items:
    if item == "stop":
        break
    print("Item:", item)

# Problem 2: Find first even number
while True:
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print("First even number found:", num)
        break

# 2. continue
# Problem 1: Skip out-of-stock items
items = ["milk", "bread", "out of stock", "eggs"]

for item in items:
    if item == "out of stock":
        continue
    print("Buy:", item)

# Problem 2: Skip even numbers
n = 10

for i in range(1, n + 1):
    if i % 2 == 0:
        continue
    print("Odd number:", i)

# 3. pass
tasks = ["email", "meeting", "call"]

for task in tasks:
    if task == "call":
        pass  # Logic to be added later
    print("Do:", task)
