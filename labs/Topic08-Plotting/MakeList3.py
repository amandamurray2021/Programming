# Q3
# Modify the program to make another array of numbers that has the salaries plus 5000.
# Author: Amanda Murray

import numpy as np 

minSalary = 20000
maxSalary = 80000
numberOfEntries = 10

np.random.seed(1) # seeding the random number generator ensuring data is the same each time the program is run.
salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)
print (salaries)

# this will add 5000 to each value
salariesPlus = salaries + 5000
print (salariesPlus)