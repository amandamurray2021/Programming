import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



data = pd.read_csv ('C:\\Users\\amand\\Desktop\\GMIT\\Programming\\pands-project2021\\iris.csv')
length = data[['sepal_length', 'petal_length']]
species = data[['class']]

xlabel = ("Length of sepals in irises")
ylabel = ("Length of petals in irises")
#legend (['iris setosa', 'iris versicolor', 'iris virginica'], loc = "upper right")

set(species)
colors = []
for z in species:
    if (z == 'setosa'):
        colors.append(0)
    elif (z == 'versicolor'):
        colors.append(1)
    else:
        z == 'virginica'
        colors.append(2)

data.plot.scatter(x = 'sepal_length', y = 'petal_length', title = 'length.py', grid = True)
plt.show()