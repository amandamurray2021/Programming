# This program plots a scatter plot with the petal length in cm on the x-axis and petal width in cm on the y-axis. 
# Using Seaborn's "hue" parameter, we pass the Iris species (class) as a third variable and save the resulting graph as a .png.
# Author: Amanda Murray

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = pd.read_csv('C:\\Users\\amand\\Desktop\\GMIT\\Programming\\pands-project2021\\iris.csv')
sns.set_style("white") # instead of using a grid, this program uses a blank white background for the scatterpoints
sns.FacetGrid(data, hue = 'class', height = 5).map(sns.scatterplot, 'petal_length', 'petal_width', s = 100).add_legend(title = 'Species')
# Notice we are calling two variables here rather than one variable for the histogram
# We use the sns.scatterplot function instead of the sns.histplot function
# We specify the size of the scatterpoints instead of selecting a number of bins to pool the data into
plt.title ('Petal lengths and widths of the iris species in the Iris data set')
plt.xlabel ('Petal length (cm)')
plt.ylabel ('Petal width (cm)')
plt.subplots_adjust (top=.9)
plt.savefig ('C:\\Users\\amand\\Desktop\\GMIT\\Programming\\pands-project2021\\scatter_petals.png')
plt.show()