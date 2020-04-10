# **************************** Challenge: Random Numbers ****************************
"""
Author: Trinity Terry
pyrun: python lists.py
"""
import random

# initiates list
my_randoms = list()

# creates a list of 10 random numbers from 1-6
for i in range(10):
    my_randoms.append(random.randrange(1, 6))

# creates a list of 10 random numbers from 1-6
numbers_1_to_10 = range(1, 11)

for number in numbers_1_to_10:
    the_numbers_match = False

    for random_number in my_randoms:
        if the_numbers_match != True:
            if random_number == number:
                the_numbers_match = True

    text = "contains" if the_numbers_match else "does not contain"
    print(f"my_random list {text} {number}")

"""
    Example Output in the Terminal
    my_randoms list contains 0
    my_randoms list does not contain 1
    my_randoms list does not contain 2
    my_randoms list contains 3
    my_randoms list contains 4
    my_randoms list does not contain 5
"""
