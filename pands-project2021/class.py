# This program plots a histogram with the iris species on the x-axis and the amount of irises on the y-axis. 
# Using Seaborn's "hue" parameter, we pass the Iris species (class) as a third variable and save the resulting graph as a .png.
# Author: Amanda Murray

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = pd.read_csv('C:\\Users\\amand\\Desktop\\GMIT\\Programming\\pands-project2021\\iris.csv')
sns.set_style("whitegrid")
sns.FacetGrid(data, hue = 'class', height = 5).map(sns.histplot, 'class', binwidth = 3).add_legend(title = 'Species')
plt.title ('Varieties of iris species in the Iris data set')
plt.xlabel ('Species')
plt.ylabel ('Number of irises')
plt.subplots_adjust (top=.9)
plt.savefig ('C:\\Users\\amand\\Desktop\\GMIT\\Programming\\pands-project2021\\class.png')
plt.show()