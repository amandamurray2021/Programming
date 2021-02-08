# floor.py
# Lab 3.2
# This program takes in a float and outputs an int rounded down
# Author: Amanda Murray

import math

numbertofloor = float (input ("enter a float number:"))
floorednumber = math.floor (numbertofloor)
print ('{} floored is {}'.format(numbertofloor, floorednumber))