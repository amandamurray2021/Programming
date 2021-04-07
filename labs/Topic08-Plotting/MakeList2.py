# Q2
# Modify the program so that the "random" salaries are the same each time the program is run.
# This will make the program easier to test or debug.
# Author: Amanda Murray

import numpy as np 

minSalary = 20000
maxSalary = 80000
numberOfEntries = 10

np.random.seed(1) # seeding the random number generator ensuring data is the same each time the program is run.
salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)
print (salaries)