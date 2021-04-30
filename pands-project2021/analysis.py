# import.py
# This program imports the Iris dataset's .data file and converts it to a .csv file for use in analysing the data set.

import pandas as pd 

filename = 'C:\\Users\\amand\\Desktop\\GMIT\\Programming\\pands-project2021\\iris.data'
workbookfilename = 'C:\\Users\\amand\\Desktop\\GMIT\\Programming\\pands-project2021\\iris.csv'
df = pd.read_csv(filename, names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])
df.to_csv(workbookfilename, index = False)
print (df)

# summary.py
# This program outputs a summary of each of the variables in the Iris data set to a .txt file (summaryofvariables.txt)

with open ('C:\\Users\\amand\\Desktop\\GMIT\\Programming\\pands-project2021\\summaryofvariables.txt', "w") as f:
    data = f.write("In the Iris data set we have 5 individual variables:\n"),
    data = f.write("1. Petal length in centimetres\n"),
    data = f.write("2. Petal width in centimetres\n"),
    data = f.write("3. Sepal length in centimetres\n"),
    data = f.write("4. Sepal width in centimetres\n"),
    data = f.write("5. Class (the species of iris flowers from the Iris data set)\n"),
    data = f.write("\n"),
    data = f.write("Here is a summary of each of the variables we will be reviewing in this project.\n"),
    data = f.write("\n"),
    data = f.write("Petal length:\n"),
    data = f.write("This is a list of 150 floats measuring the length of petals in centimetres in the following iris species:\n"),
    data = f.write("Iris-setosa, Iris-versicolor and Iris-virginica.\n"),
    data = f.write("\n"),
    data = f.write("Petal width:\n"),
    data = f.write("This is a list of 150 floats measuring the width of petals in centimetres in the following iris species:\n"),
    data = f.write("Iris-setosa, Iris-versicolor and Iris-virginica.\n"),
    data = f.write("\n"),
    data = f.write("Sepal length:\n"),
    data = f.write("This is a list of 150 floats measuring the length of sepals in centimetres in the following iris species:\n"),
    data = f.write("Iris-setosa, Iris-versicolor and Iris-virginica.\n"),
    data = f.write("\n"),
    data = f.write("Sepal width:\n"),
    data = f.write("This is a list of 150 floats measuring the width of sepals in centimetres in the following iris species:\n"),
    data = f.write("Iris-setosa, Iris-versicolor and Iris-virginica.\n"),
    data = f.write("\n"),
    data = f.write("Class:\n"),
    data = f.write("This is a list of 150 names of the Iris species in the data set: Iris-setosa, Iris-versicolor and Iris-virginica.\n"),
    data = f.write("There are 50 of Iris-setosa, 50 of Iris-versicolor and 50 of Iris-virginica.\n"),
    data = f.write("\n"),
    data = f.write("Using Matplotlib, Pandas and Seaborn:\n"),
    data = f.write("* We are going to plot each of these variables in histograms against their class.\n"), 
    data = f.write("* We are going to plot pairs of variables in scatterplots against their class.\n")

# petallength.py
# This program plots a histogram with petal length in cm on the x-axis and the amount of irises on the y-axis. 
# Using Seaborn's "hue" parameter, we pass the Iris species (class) as a third variable and save the resulting graph as a .png.

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = pd.read_csv('C:\\Users\\amand\\Desktop\\GMIT\\Programming\\pands-project2021\\iris.csv')
sns.set_style("whitegrid")
sns.FacetGrid(data, hue = 'class', height = 5).map(sns.histplot, 'petal_length', bins = 5).add_legend(title = 'Species')
plt.title ('Petal lengths of the iris species in the Iris data set')
plt.xlabel ('Petal length (cm)')
plt.ylabel ('Number of irises')
plt.subplots_adjust (top=.9)
plt.savefig ('C:\\Users\\amand\\Desktop\\GMIT\\Programming\\pands-project2021\\petal_length.png')
plt.show()

# petalwidth.py
# This program plots a histogram with petal width in cm on the x-axis and the amount of irises on the y-axis. 
# Using Seaborn's "hue" parameter, we pass the Iris species (class) as a third variable and save the resulting graph as a .png.

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = pd.read_csv('C:\\Users\\amand\\Desktop\\GMIT\\Programming\\pands-project2021\\iris.csv')
sns.set_style("whitegrid")
sns.FacetGrid(data, hue = 'class', height = 5).map(sns.histplot, 'petal_width', bins = 5).add_legend(title = 'Species')
plt.title ('Petal widths of the iris species in the Iris data set')
plt.xlabel ('Petal width (cm)')
plt.ylabel ('Number of irises')
plt.subplots_adjust (top=.9)
plt.savefig ('C:\\Users\\amand\\Desktop\\GMIT\\Programming\\pands-project2021\\petal_width.png')
plt.show()

# sepallength.py
# This program plots a histogram with sepal length in cm on the x-axis and the amount of irises on the y-axis. 
# Using Seaborn's "hue" parameter, we pass the Iris species (class) as a third variable and save the resulting graph as a .png.

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = pd.read_csv('C:\\Users\\amand\\Desktop\\GMIT\\Programming\\pands-project2021\\iris.csv')
sns.set_style("whitegrid")
sns.FacetGrid(data, hue = 'class', height = 5).map(sns.histplot, 'sepal_length', bins = 5).add_legend(title = 'Species')
plt.title ('Sepal lengths of the iris species in the Iris data set')
plt.xlabel ('Sepal length (cm)')
plt.ylabel ('Number of irises')
plt.subplots_adjust (top=.9)
plt.savefig ('C:\\Users\\amand\\Desktop\\GMIT\\Programming\\pands-project2021\\sepal_length.png')
plt.show()

# sepalwidth.py
# This program plots a histogram with sepal width in cm on the x-axis and the amount of irises on the y-axis. 
# Using Seaborn's "hue" parameter, we pass the Iris species (class) as a third variable and save the resulting graph as a .png.

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

# class.py
# This program plots a histogram with the iris species on the x-axis and the amount of irises on the y-axis. 
# Using Seaborn's "hue" parameter, we pass the Iris species (class) as a third variable and save the resulting graph as a .png.

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

# scatterpetals.py
# This program plots a scatter plot with the petal length in cm on the x-axis and petal width in cm on the y-axis. 
# Using Seaborn's "hue" parameter, we pass the Iris species (class) as a third variable and save the resulting graph as a .png.

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = pd.read_csv('C:\\Users\\amand\\Desktop\\GMIT\\Programming\\pands-project2021\\iris.csv')
sns.set_style("white")
sns.FacetGrid(data, hue = 'class', height = 5).map(sns.scatterplot, 'petal_length', 'petal_width', s = 100).add_legend(title = 'Species')
plt.title ('Petal lengths and widths of the iris species in the Iris data set')
plt.xlabel ('Petal length (cm)')
plt.ylabel ('Petal width (cm)')
plt.subplots_adjust (top=.9)
plt.savefig ('C:\\Users\\amand\\Desktop\\GMIT\\Programming\\pands-project2021\\scatter_petals.png')
plt.show()

# scattersepals.py
# This program plots a scatter plot with the sepal length in cm on the x-axis and sepal width in cm on the y-axis. 
# Using Seaborn's "hue" parameter, we pass the Iris species (class) as a third variable and save the resulting graph as a .png.

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = pd.read_csv('C:\\Users\\amand\\Desktop\\GMIT\\Programming\\pands-project2021\\iris.csv')
sns.set_style("white")
sns.FacetGrid(data, hue = 'class', height = 5).map(sns.scatterplot, 'sepal_length', 'sepal_width', s = 100).add_legend(title = 'Species')
plt.title ('Sepal lengths and widths of the iris species in the Iris data set')
plt.xlabel ('Sepal length (cm)')
plt.ylabel ('Sepal width (cm)')
plt.subplots_adjust (top=.9)
plt.savefig ('C:\\Users\\amand\\Desktop\\GMIT\\Programming\\pands-project2021\\scatter_sepals.png')
plt.show()

# scatterlength.py
# This program plots a scatter plot with the petal length in cm on the x-axis and sepal length in cm on the y-axis. 
# Using Seaborn's "hue" parameter, we pass the Iris species (class) as a third variable and save the resulting graph as a .png.

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = pd.read_csv('C:\\Users\\amand\\Desktop\\GMIT\\Programming\\pands-project2021\\iris.csv')
sns.set_style("white")
sns.FacetGrid(data, hue = 'class', height = 5).map(sns.scatterplot, 'petal_length', 'sepal_length', s = 100).add_legend(title = 'Species')
plt.title ('Petal and sepal lengths of the iris species in the Iris data set')
plt.xlabel ('Petal length (cm)')
plt.ylabel ('Sepal length (cm)')
plt.subplots_adjust (top=.9)
plt.savefig ('C:\\Users\\amand\\Desktop\\GMIT\\Programming\\pands-project2021\\scatter_length.png')
plt.show()

# scatterwidth.py
# This program plots a scatter plot with the petal width in cm on the x-axis and sepal width in cm on the y-axis. 
# Using Seaborn's "hue" parameter, we pass the Iris species (class) as a third variable and save the resulting graph as a .png.

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = pd.read_csv('C:\\Users\\amand\\Desktop\\GMIT\\Programming\\pands-project2021\\iris.csv')
sns.set_style("white")
sns.FacetGrid(data, hue = 'class', height = 5).map(sns.scatterplot, 'petal_width', 'sepal_width', s = 100).add_legend(title = 'Species')
plt.title ('Petal and sepal widths of the iris species in the Iris data set')
plt.xlabel ('Petal width (cm)')
plt.ylabel ('Sepal width (cm)')
plt.subplots_adjust (top=.9)
plt.savefig ('C:\\Users\\amand\\Desktop\\GMIT\\Programming\\pands-project2021\\scatter_width.png')
plt.show()