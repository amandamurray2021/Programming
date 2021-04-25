import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv ('C:\\Users\\amand\\Desktop\\GMIT\\Programming\\pands-project2021\\iris.csv')
species = pd.DataFrame(data, columns = ['class'])
species['class'] = pd.to_numeric(species['class'], errors = 'coerce')
pd.DataFrame.hist (species, grid = False)


plt.xlabel ('Species of iris')
plt.ylabel ('Amount of irises')
plt.show()

