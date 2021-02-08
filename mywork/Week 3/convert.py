# convert.py
# Lab 3.2
# This program takes in a float amount in $ and returns the absolute amount in ¢
# Author: Amanda Murray

import math

dollars = float (input ("please enter a $ amount:"))
cents = abs (int (dollars * 100.0))
print ('that amount in ¢ is {}'.format (cents))