# This program plots a histogram with sepal width in cm on the x-axis and the amount of irises on the y-axis. 
# Using Seaborn's "hue" parameter, we pass the Iris species (class) as a third variable and save the resulting graph as a .png.
# Author: Amanda Murray

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = pd.read_csv('C:\\Users\\amand\\Desktop\\GMIT\\Programming\\pands-project2021\\iris.csv')
sns.set_style("whitegrid")
sns.FacetGrid(data, hue = 'class', height = 5).map(sns.histplot, 'sepal_width', bins = 5).add_legend(title = 'Species')
plt.title ('Sepal widths of the iris species in the Iris data set')
plt.xlabel ('Sepal width (cm)')
plt.ylabel ('Number of irises')
plt.subplots_adjust (top=.9)
plt.savefig ('C:\\Users\\amand\\Desktop\\GMIT\\Programming\\pands-project2021\\sepal_width.png')
plt.show()