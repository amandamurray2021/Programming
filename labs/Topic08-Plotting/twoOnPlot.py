# Q9
# Q8
# Add a line to the scatter plot from Q7 that shows y = x² in a different colour.
# Author: Amanda Murray

import numpy as np 
import matplotlib.pyplot as plt 

minSalary = 20000
maxSalary = 80000
numberOfEntries = 10

np.random.seed(1) # seeding the random number generator ensuring data is the same each time the program is run.
salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)
ages = np.random.randint (low=21, high=65, size=numberOfEntries)

plt.scatter(ages,salaries)

# add x squared
xpoints = np.array (range(1, 101))
ypoints = xpoints * xpoints

plt.plot (xpoints, ypoints, color= 'r')
plt.show() # see how the axis have changed