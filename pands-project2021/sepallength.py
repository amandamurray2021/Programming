# This program plots a histogram with sepal length in cm on the x-axis and the amount of irises on the y-axis. 
# Using Seaborn's "hue" parameter, we pass the Iris species (class) as a third variable and save the resulting graph as a .png.
# Author: Amanda Murray

import matplotlib.pyplot as plt # a low level graph plotting library in Python
import pandas as pd # a Python library used for working with datasets
import seaborn as sns # A library that uses matplotlib underneath to plot graphs

data = pd.read_csv('C:\\Users\\amand\\Desktop\\GMIT\\Programming\\pands-project2021\\iris.csv') 
sns.set_style("whitegrid")
sns.FacetGrid(data, hue = 'class', height = 5).map(sns.histplot, 'sepal_length', bins = 5).add_legend(title = 'Species')
plt.title ('Sepal lengths of the iris species in the Iris data set')
plt.xlabel ('Sepal length (cm)')
plt.ylabel ('Number of irises')
plt.subplots_adjust (top=.9)
plt.savefig ('C:\\Users\\amand\\Desktop\\GMIT\\Programming\\pands-project2021\\sepal_length.png')
plt.show()