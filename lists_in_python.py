# LISTS
# Indexing lists
numbers = [2, 43, 87, 5]
print(f'Original list: {numbers}')
# lets replace the first element using index
numbers[0] = 50
print(f'Edited list: {numbers}')
# lets the value of an element to another element in the same list
numbers[1] = numbers[3] # 2ND TO LAST
print(f'Edited list: {numbers}')

# Accessing list content
print(numbers[1]) # prints an element in the list
print(numbers) # prints the entire list

# The len() function
print(len(numbers))

# Removing elements from a list
del numbers[3] # this deletes the last item
print(len(numbers)) # len reduces by 1.

# Negative indices
# this count from the last element in the list
print(numbers[-1]) # prints last element
print(numbers[-2]) # prints 2nd to the last element

# Task on lists
hat_num = [1, 2, 3, 4, 5]
user_num = int(input('Enter a number: '))
user_num = hat_num[2]
del hat_num[-1]
print(len(hat_num))

# Adding elements to a list: append() and insert()
# append() is used to add a new element to the end of a list
digit = [44, 32, 3, 98, 70]
print(len(digit)) 
digit.append(32) # this adds 32 to the end of the list
print(digit)
print(len(digit)) # increases by 1

# insert() is used to add a new element to any part of the list
digit.insert(2, 67) # this assigns 67 to the 3RD position in the list
print(digit)
print(len(digit))  # increases by 1

# adding multiple elements to a list
# lets start with an empty list
numb = [ ]
for i in range(5): # starts from 0 and ends at 4
    numb.append(i + 1) # so we add 1

print(numb)

# inseert() to get the reverse order
numb = [ ]
for i in range(5):
    numb.insert(0, i + 1) # this initializes each input as the first

print(numb)

# Making use of lists
# using for loops
new_list = [2, 4, 1, 9, 7]
total = 0
# a program to find the sum of all elemnts in a list
for i in range(len(new_list)):
    #lets connects each number from 0 - 4 to its corresponding value in the list
    total += new_list[i]

print(total)

# The second aspect of the for loop
# an alternative way to find sum
# using for loops
new_list = [2, 4, 1, 9, 7]
total = 0
for i in new_list:
    total += i

print(total) # returns same output


#  Lists in action
# swapping elements in a list.
new_list = [2, 4, 1, 9, 7]
print(new_list)
# the swap
new_list[1], new_list[3] = new_list[3], new_list[1]
print(new_list)
# sadly this method is limited

# using for loops to swap
length = len(new_list)
for i in range(length // 2):
    new_list[i], new_list[length - i - 1] = new_list[length - i - 1], new_list[i]

print(new_list)

# NESTED LISTS 
my_list = [1, 'a', ["list", 64, [0, 1], False]]

# 3.5 Section 5 – Sorting simple lists: the bubble sort algorithm
# The bubble sort
# this is simply swapping consecutive elements of a list under a given restriction
# using python sorting
a_list = [2, 9, 5, 43, 12]
a_list.sort()
print(a_list)
a_list.reverse()
print(a_list)