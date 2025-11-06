# 3.6 Section 6 – Operations on lists
# The inner life of lists
a = 2
b = a
a = 3
print(b) # b remains 2
# for lists
a = [2]
b = a
a[0] = 7
print(b) # b becomes 7 too
# in list the assignment of a = b: links both lists to save memory storage
# i.e they'll for same thing

# Powerful slices
# A slice is an element of Python syntax that allows you to make a brand new copy of a list, or parts of a list.
# its represented by ':'
a = [2]
b = a[:]
a[0] = 7
print(b) # b remains 2

# SLICES WORKING LIKE INDEX
a = [3, 5, 9, 6, 1]
b = a[ 1 : 4] # starts from the 2nd till the 4th
# the first number represents the index of the first element, 
# the second represents index of the first element not included
# '4 - 1' gives the number of the elements in the new list
print(b)

# Slices – negative indices
a = [3, 5, 9, 6, 1]
b = a[ 1 : -1] # starts from second, ommits last
# in python [: 4] = [0:4]
# if you ommit the start index it starts from '0'
a = [3, 5, 9, 6, 1]
b = a[:3]
print(b)
# Similarly, if you omit the end in your slice,
# it is assumed that you want the slice to end at the element with the index len(my_list).
a = [3, 5, 9, 6, 1]
b = a[2:]
print(b)

# More about the del instruction
# using del to delete part of a list
a = [3, 5, 9, 6, 1]
del a[1:3]
print(a)
# it can all delete all the content in a list
a = [3, 5, 9, 6, 1]
del a[:]
print(a) # this prints an empty list
# this is different from
a = [3, 5, 9, 6, 1]
del a
# print(a) # this prints an error

# The in and not in operators
# these look through the list in order to check whether a specific value is stored inside the list or not.
a = [1, 4, 7, 9, 2, 4, 8, 3]
print(23 in a)
print( 23 not in a)
print(1 in a)
print(1 not in a)

# Lists – some simple programs
# finding the largest number in a list
a = [1, 4, 7, 9, 2, 4, 8, 3]
largest = a[0] # setting a intial value
for i in range(1, len(a)): # the range limit is the index of the last element
    if a[i] > largest:
        largest = a[i] # setting a new value

print(largest)

# a simpler form
a = [1, 4, 7, 9, 2, 4, 8, 3]
largest = a[0] 
for i in a:
    if i > largest:
        largest = i

print(largest) # same output

# finding the location of a given element inside a list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5
found = False

for i in range(len(my_list)):
    found = my_list[i] == to_find
    if found:
        break

if found:
    print("Element found at index", i)
else:
    print("absent")

# program to find how many hits one has in a lottery
drawn = [5, 11, 9, 42, 3, 49]
bets = [3, 7, 11, 42, 34, 49]
hits = 0
for i in drawn:
    if i in bets:
        hits += 1

print(hits)

# program to remove repitions in a list
# Original list 
numbers = [2, 3, 5, 2, 7, 5, 9, 3, 1, 9, 7, 4]

# Create a new list without repetitions
unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

# Display results
print("Original list:", numbers)
print("List without repetitions:", unique_numbers)

# SUMMARY
# If you have a list list_1, then the following assignment: list_2 = list_1
#  does not make a copy of the list_1 list, 
# but makes the variables list_1 and list_2 point to one and the same list in memory. 
# for example
vehicles_one = ['car', 'bicycle', 'motor']
print(vehicles_one) # outputs: ['car', 'bicycle', 'motor']

vehicles_two = vehicles_one
del vehicles_one[0] # deletes 'car'
print(vehicles_two) # outputs: ['bicycle', 'motor']

# 2. If you want to copy a list or part of the list, you can do it by performing slicing:
colors = ['red', 'green', 'orange']

copy_whole_colors = colors[:]  # copy the entire list
copy_part_colors = colors[0:2]  # copy part of the list

# 3. You can use negative indices to perform slices, too. For example:
sample_list = ["A", "B", "C", "D", "E"]
new_list = sample_list[2:-1]
print(new_list)  # outputs: ['C', 'D']

# 4. The start and end parameters are optional when performing a slice: list[start:end], e.g
my_list = [1, 2, 3, 4, 5]
slice_one = my_list[2: ]
slice_two = my_list[ :2]
slice_three = my_list[-2: ]

print(slice_one)  # outputs: [3, 4, 5]
print(slice_two)  # outputs: [1, 2]
print(slice_three)  # outputs: [4, 5]


# 2D LISTS
alphas = ['a', 'b', 'c', 'd']
digits = ['1', '2', '3', '4']
random = ['buy', 'rio', 'pie', 'tie']

list_2d = [alphas, digits, random]

print(list_2d[1]) # prints digits
# lets print '3'
print(list_2d[1][2])
# lets print 'rio'
print(list_2d[2][1])

# to print a list to seperate lines
for i in list_2d:
    for a in i:
        print(a) # this list every item on separate lines

# creating a keypad with 2D LISTS
num_pad = ((1, 2, 3),
           (4, 5, 6),
           ('*', 0, '#'))

for i in num_pad:
    for x in i:
        print(x, end= " ")
    print()
