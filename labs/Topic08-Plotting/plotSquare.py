# Q5
# Write a program that plots the function y = x²
# Author: Amanda Murray

import matplotlib.pyplot as plt 
import numpy as np 

xpoints = np.array(range(1,101))
ypoints = xpoints * xpoints # multiply each entry by itself

plt.plot (xpoints, ypoints)
plt.show()