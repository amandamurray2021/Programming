# Q9
# Add a legend, title and axis labels to the scatter plot from Q7.
# Author: Amanda Murray

import numpy as np 
import matplotlib.pyplot as plt 

minSalary = 20000
maxSalary = 80000
numberOfEntries = 10

np.random.seed(1) # seeding the random number generator ensuring data is the same each time the program is run.
salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)
ages = np.random.randint (low=21, high=65, size=numberOfEntries)

plt.scatter(ages,salaries, label = "salaries")

# add x squared
xpoints = np.array (range(1, 101))
ypoints = xpoints * xpoints

plt.plot (xpoints, ypoints, color= 'r', label = "x squared")
plt.title ("random plot")
plt.xlabel ("age")
plt.ylabel ("salaries")
plt.legend()
# plt.show() # see how the axis have changed
plt.savefig ('prettier-plot.png')