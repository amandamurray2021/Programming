# Q1
# This program makes a list called "salaries" that has 10 random numbers between 20000 to 80000
# Author: Amanda Murray

import numpy as np 
# it is a good idea to have your absolute values set into variables at the beginning of your program.

minSalary = 20000
maxSalary = 80000
numberOfEntries = 10

salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)
print (salaries)

