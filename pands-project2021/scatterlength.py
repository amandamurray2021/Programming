# This program plots a scatter plot with the petal length in cm on the x-axis and sepal length in cm on the y-axis. 
# Using Seaborn's "hue" parameter, we pass the Iris species (class) as a third variable and save the resulting graph as a .png.
# Author: Amanda Murray

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = pd.read_csv('C:\\Users\\amand\\Desktop\\GMIT\\Programming\\pands-project2021\\iris.csv')
sns.set_style("white")
sns.FacetGrid(data, hue = 'class', height = 5).map(sns.scatterplot, 'petal_length', 'sepal_length', s = 100).add_legend(title = 'Species')
plt.title ('Petal and sepal lengths of the iris species in the Iris data set')
plt.xlabel ('Petal length (cm)')
plt.ylabel ('Sepal length (cm)')
plt.subplots_adjust (top=.9)
plt.savefig ('C:\\Users\\amand\\Desktop\\GMIT\\Programming\\pands-project2021\\scatter_length.png')
plt.show()