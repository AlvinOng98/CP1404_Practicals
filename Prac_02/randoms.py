"""
CP1404/CP5632 - Practical 2
Student Name: Alvin Ong Zhi Xiang

Randoms
"""

import random
print(random.randint(5, 20))  # line 1
# Smallest number is 5 and largest number is 20

print(random.randrange(3, 10, 2))  # line 2
# Smallest number is 3 and largest number is 9
# It could not have produced a 4 because the range only included odd numbers
# as they are in steps of 2, starting from 3

print(random.uniform(2.5, 5.5))  # line 3
# Smallest number could have seen is 2.5 and largest number is 5.5

print(random.randint(1, 100)) # random number between 1 and 100 inclusive