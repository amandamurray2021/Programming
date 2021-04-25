import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv ('C:\\Users\\amand\\Desktop\\GMIT\\Programming\\pands-project2021\\iris.csv')
petal_length = pd.DataFrame(data, columns = ['petal_length'])
pd.DataFrame.hist (petal_length, grid = False)

font1 = {'family': 'serif', 'color': 'black', 'size': 15} # this determines the font, color and size of the title
font2 = {'family': 'serif', 'color': 'purple', 'size': 15} # this determines the font, color and size of the xlabel
font3 = {'family': 'serif', 'color': 'orange', 'size': 15} # this determines the font, color and size of the ylabel

plt.title('petal_length.py', fontdict = font1)
plt.xlabel ('Length of petals(cm)', fontdict = font2)
plt.ylabel ('Amount of irises', fontdict = font3)
plt.show()