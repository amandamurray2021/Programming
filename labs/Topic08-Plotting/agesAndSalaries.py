# Q7
# Write a program that makes a list called ages that has the same random number values as salaries.
# Range: 21 to 65.
# Make a scatter plot of this data.

import numpy as np 
import matplotlib.pyplot as plt 

minSalary = 20000
maxSalary = 80000
numberOfEntries = 10

np.random.seed(1) # seeding the random number generator ensuring data is the same each time the program is run.
salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)
ages = np.random.randint (low=21, high=65, size=numberOfEntries)

plt.scatter(ages,salaries)
plt.show()