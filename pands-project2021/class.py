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


iris = data['class']
if iris (range(0,49)):
    print ("iris setosa")
elif species (range(50,99)):
    print ("iris versicolor")
else:
    species (range(100,149))
    print ("iris virginica")

if species < 0 or species <= 49: # we know it is greater than 0
    print ("iris setosa")
elif species > 50 or species <= 99: # between 40 and 49
    print ("iris versicolor")
else: # the only option left is between 70 and 100
    species > 100 or species <= 149
    print ("iris virginica")

# iris 0 - 49 = setosa
# iris 50 - 99 = versicolor
# iris 100 - 149 = virginica
