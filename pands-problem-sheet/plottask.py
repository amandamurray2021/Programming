# Weekly Task 8
# This program will display a plot of the following functions:
# f(x) = x
# g(x) = x²
# h(x) = x³
# It will be in the range [0, 4] on one set of axes.
# Author: Amanda Murray

import matplotlib.pyplot as plt # to visualise the graph
import numpy as np # for working with arrays

x = np.array (range(0, 4)) # f(x) = x
g = x * x # g(x) = x²
h = x * x * x # h(x) = x³

font1 = {'family': 'serif', 'color': 'black', 'size': 15} # this determines the font, color and size of the title
font2 = {'family': 'serif', 'color': 'purple', 'size': 15} # this determines the font, color and size of the xlabel
font3 = {'family': 'serif', 'color': 'orange', 'size': 15} # this determines the font, color and size of the ylabel

plt.plot (x, color = 'pink', marker = 'o') # this marks x on the plot in pink with markers for the points
plt.plot (g, color = 'purple', marker = 'o') # this marks g on the plot in purple with markers for the points
plt.plot (h, color = 'orange', marker = 'o') # this marks h on the plot in orange with markers for the points
plt.title ("plottask.py", fontdict = font1)
plt.xlabel ("g = x²", fontdict = font2)
plt.ylabel ("h = x³", fontdict = font3)
plt.savefig ('plottask.png')
plt.show()