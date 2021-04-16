# Weekly Task 8
# This program will display a plot of the following functions:
# f(x) = x
# g(x) = x²
# h(x) = x³
# It will be in the range [0, 4] on the one set of axes.
# Author: Amanda Murray

import matplotlib.pyplot as plt 
import numpy as np 
x = (range (0,4))

x = np.array (range(0, 4))
g = x * x
h = x * x * x

font1 = {'family': 'serif', 'color': 'black', 'size': 15}
font2 = {'family': 'serif', 'color': 'purple', 'size': 15}
font3 = {'family': 'serif', 'color': 'orange', 'size': 15}

plt.plot (x, color = 'pink', marker = 'o')
plt.plot (g, color = 'purple', marker = 'o')
plt.plot (h, color = 'orange', marker = 'o')
plt.title ("plottask.py", fontdict = font1)
plt.xlabel ("g = x²", fontdict = font2)
plt.ylabel ("h = x³", fontdict = font3)
plt.savefig ('plottask.png')
plt.show()