# This program plots a scatter plot with the sepal length in cm on the x-axis and sepal width in cm on the y-axis. 
# Using Seaborn's "hue" parameter, we pass the Iris species (class) as a third variable and save the resulting graph as a .png.
# Author: Amanda Murray

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = pd.read_csv('C:\\Users\\amand\\Desktop\\GMIT\\Programming\\pands-project2021\\iris.csv')
sns.set_style("white")
sns.FacetGrid(data, hue = 'class', height = 5).map(sns.scatterplot, 'sepal_length', 'sepal_width', s = 100).add_legend(title = 'Species')
plt.title ('Sepal lengths and widths of the iris species in the Iris data set')
plt.xlabel ('Sepal length (cm)')
plt.ylabel ('Sepal width (cm)')
plt.subplots_adjust (top=.9)
plt.savefig ('C:\\Users\\amand\\Desktop\\GMIT\\Programming\\pands-project2021\\scatter_sepals.png')
plt.show()