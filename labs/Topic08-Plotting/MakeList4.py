# Q4
# Modify the program so that it increases all of the salaries by 5%.
# Store these numbers in a different array.
# Author: Amanda Murray

import numpy as np 

minSalary = 20000
maxSalary = 80000
numberOfEntries = 10

np.random.seed(1) # seeding the random number generator ensuring data is the same each time the program is run.
salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)
print (salaries)

salariesMult = salaries * 1.05 # add 5% by multiplying by 1.05
print (salariesMult)
# this returns a float array
# to convert to an int array:
newSalaries = salariesMult.astype(int)
print (newSalaries)