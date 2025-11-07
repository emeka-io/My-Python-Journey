# Solving problems using loops
# multiplication table in a single line using for loop till n * 10.
# take input
n = int(input())

# print multiplication table in one line
for i in range(1, 11):
    print(n * i, end=" ")


# 2 jump
# take input
s = input()

# print characters at even indices
for i in range(0, len(s)):
    if i % 2 == 0:
        print(s[i], end="")


# alternate version
def stringJumper(s):
    for i in range(0, len(s), 2):
        # from 0 to length of str and skip 2
        print(s[i], end="")
        # printing character and separating characters by nothing

#printing numbers from x to 0 in decreasing order in a single line.
def printInDecreasing(x):
    # code here
    while (x >= 0):
        # print number in decreasing order
        print(x, end=" ")
        x -= 1


# Find the factorial of n.
class Solution:
    # Function to calculate factorial of a number.
    def factorial(self, n: int) -> int:
        # code here
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact


#.Given an integer n, write a program to print the square of size n using "*" character.
# take input
n = int(input())

# loop through rows
for i in range(n):
    for j in range(n):
        # print * for first/last row OR first/last column
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()  # move to next line after each row
