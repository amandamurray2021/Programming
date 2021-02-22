# randomfruit.py
# Lab 2.3
# This program prints out a random fruit
# Author: Amanda Murray

import random

fruits = ('apple', 'orange', 'banana', 'pear')

# we want a random number between 0 and length -1
index = random.randint(0, len(fruits)-1)

fruit = fruits [index]
print ('a random fruit: {}'.format (fruit))