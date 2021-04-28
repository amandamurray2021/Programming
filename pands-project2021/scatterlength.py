import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv ('C:\\Users\\amand\\Desktop\\GMIT\\Programming\\pands-project2021\\iris.csv')
x = pd.DataFrame(data, columns = ['sepal_length'])
y = pd.DataFrame(data, columns = ['petal_length'])
c = colors
#s = 100
#species = pd.DataFrame(data, columns = ['class'])
#species['class'] = pd.to_numeric(species['class'], errors = 'coerce')
plt.scatter (x, y, c)

#plt.xlabel = ("Length of sepals in irises")
#plt.ylabel = ("Length of petals in irises")

def species():
    with open (data) as f:
        z = (f.pd.DataFrame(data, columns = ['class'])
        colors = ([])
    for z in species:
        if (z == 'setosa'):
        colors.append(0)
        if (z == 'versicolor'):
        colors.append(1)
        if (z == 'virginica'):
        colors.append(2)
return colors



#set (species)
#colors = []
#for z in species:
#    if (z == 'setosa'):
#        colors.append(0)
#    if (z == 'versicolor'):
#        colors.append(1)
#    if (z == 'virginica'):
#        colors.append(2)

viridis = plt.cm.get_cmap('viridis', 3)

legend_aliases = [
    plt.scatter ([], [], label ='setosa', c = viridis(0))
    plt.scatter ([], [], label ='versicolor', c = viridis(1))
    plt.scatter ([], [], label ='virginica', c = viridis(2))
]
plt.legend(handles= legend_aliases)
plt.show()