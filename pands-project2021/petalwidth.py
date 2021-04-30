# This program plots a histogram with petal width in cm on the x-axis and the amount of irises on the y-axis. 
# Using Seaborn's "hue" parameter, we pass the Iris species (class) as a third variable and save the resulting graph as a .png.
# Author: Amanda Murray

import matplotlib.pyplot as plt # a low level graph plotting library in Python
import pandas as pd # a Python library used for working with datasets
import seaborn as sns # A library that uses matplotlib underneath to plot graphs

data = pd.read_csv('C:\\Users\\amand\\Desktop\\GMIT\\Programming\\pands-project2021\\iris.csv') # importing the .csv file
sns.set_style("whitegrid")
sns.FacetGrid(data, hue = 'class', height = 5).map(sns.histplot, 'petal_width', bins = 5).add_legend(title = 'Species')
# Using the Facet Grid, we can assign petal width to the x-axis and the amount of irises on the y-axis.
# Using the 'hue' parameter, we can assign a third variable (class) in different colours.
# height refers to the height in inches of the grid
# Using sns.histplot to generate the histogram
# Using bins to pool the data
# Adding a legend for the colours
plt.title ('Petal widths of the iris species in the Iris data set') # set the title
plt.xlabel ('Petal width (cm)') # set title of x-axis
plt.ylabel ('Number of irises') # set title of y-axis
plt.subplots_adjust (top=.9) # adjust the size of the graph to prevent title being cut off
plt.savefig ('C:\\Users\\amand\\Desktop\\GMIT\\Programming\\pands-project2021\\petal_width.png') # save the figure generated
plt.show() # show the figure generated