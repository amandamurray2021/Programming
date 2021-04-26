import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv ('C:\\Users\\amand\\Desktop\\GMIT\\Programming\\pands-project2021\\iris.csv')
sepal_width = pd.DataFrame(data, columns = ['sepal_width'])
pd.DataFrame.hist (sepal_width, grid = False)

font1 = {'family': 'serif', 'color': 'black', 'size': 15} # this determines the font, color and size of the title
font2 = {'family': 'serif', 'color': 'purple', 'size': 15} # this determines the font, color and size of the xlabel
font3 = {'family': 'serif', 'color': 'orange', 'size': 15} # this determines the font, color and size of the ylabel

plt.title('sepal_width.py', fontdict = font1)
plt.xlabel ('Width of sepals (cm)', fontdict = font2)
plt.ylabel ('Amount of irises', fontdict = font3)
plt.show()








sepal_width = pd.DataFrame(data, columns = ['sepal_width','class'])
sepal_width['class'] = pd.to_numeric(sepal_width['class'], errors = 'coerce')
plt.hist (sepal_width)
plt.show()