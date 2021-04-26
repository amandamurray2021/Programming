import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv ('C:\\Users\\amand\\Desktop\\GMIT\\Programming\\pands-project2021\\iris.csv')
width = pd.DataFrame(data, columns = ['sepal_width', 'petal_width'])
#species = data[['class']]

xlabel = ("Width of sepals in irises")
ylabel = ("Width of petals in irises")
#legend (['iris setosa', 'iris versicolor', 'iris virginica'], loc = "upper right")

#set(species)
#colors = []
#for z in species:
#    if (z == 'setosa'):
#        colors.append(0)
#    elif (z == 'versicolor'):
#        colors.append(1)
#    else:
#        z == 'virginica'
#        colors.append(2)
#colors

data.plot.scatter(x = 'sepal_width', y = 'petal_width', title = 'width.py', s = 100)
plt.show()