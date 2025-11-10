# GENERATING RANDOM VALUES USING PACKAGES IN PYTHON
import random
for i in range(3):
    print(random.random()) # this picks random values from 0 - 1

# now let's set our range
for i in range(3):
    print(random.randint(3,10))

for i in range(3):
    print(random.randint(3,10))

# note: both give diff random values

# picking a random person from a list of members to be evicted
members = ['rio', 'bob', 'jane', 'luis']
import random
evict = random.choice(members)
print(f"Sorry {evict}, you've been evicted")

# generating random dice roll results
import random

class Dice:
    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1,6)
        return (first, second)
    

dice = Dice()
print(dice.roll())
print(dice.roll())
print(dice.roll()) # these give three random results