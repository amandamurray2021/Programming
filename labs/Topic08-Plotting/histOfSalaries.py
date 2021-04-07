# Q6
# Write a program that plots a histogram of the salaries (from Q1).
# Author: Amanda Murray

import numpy as np 
import matplotlib.pyplot as plt 

minSalary = 20000
maxSalary = 80000
numberOfEntries = 10

np.random.seed(1) # seeding the random number generator ensuring data is the same each time the program is run.
salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)

plt.hist(salaries)
plt.show()