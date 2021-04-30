# import.py
# This program imports the Iris dataset's .data file and converts it to a .csv file for use in analysing the data set.
# Author: Amanda Murray

import pandas as pd # A Python library used for working with datasets

filename = 'C:\\Users\\amand\\Desktop\\GMIT\\Programming\\pands-project2021\\iris.data'
# importing the .data file and specifying the path so the file is imported from the correct location
workbookfilename = 'C:\\Users\\amand\\Desktop\\GMIT\\Programming\\pands-project2021\\iris.csv'
# converting the .data file to a .csv file and specifying the path so it's saved in the right sub-folder of my repository
df = pd.read_csv(filename, names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']) # importing all the variables
df.to_csv(workbookfilename, index = False) # used index = False to remove the numerical index so the data isn't skewed for analysis
print (df)

# summary.py
# This program outputs a summary of each of the variables in the Iris data set to a .txt file (summaryofvariables.txt)
# Author: Amanda Murray

with open ('C:\\Users\\amand\\Desktop\\GMIT\\Programming\\pands-project2021\\summaryofvariables.txt', "w") as f: # open the .txt file to write
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

# use data = f.write() for each line you want to write
# running the code will write it to the summaryofvariables.txt file

# petallength.py
# This program plots a histogram with petal length in cm on the x-axis and the amount of irises on the y-axis. 
# Using Seaborn's "hue" parameter, we pass the Iris species (class) as a third variable and save the resulting graph as a .png.
# Author: Amanda Murray

import matplotlib.pyplot as plt # a low level graph plotting library in Python
import pandas as pd # a Python library used for working with datasets
import seaborn as sns # A library that uses matplotlib underneath to plot graphs

data = pd.read_csv('C:\\Users\\amand\\Desktop\\GMIT\\Programming\\pands-project2021\\iris.csv') # importing the .csv file
sns.set_style("whitegrid") # setting the style of the histogram to include a grid
sns.FacetGrid(data, hue = 'class', height = 5).map(sns.histplot, 'petal_length', bins = 5).add_legend(title = 'Species')
# Using the Facet Grid, we can assign petal length to the x-axis and the amount of irises on the y-axis.
# Using the 'hue' parameter, we can assign a third variable (class) in different colours.
# height refers to the height in inches of the grid
# Using sns.histplot to generate the histogram
# Using bins to pool the data
# Adding a legend for the colours
plt.title ('Petal lengths of the iris species in the Iris data set') # set title
plt.xlabel ('Petal length (cm)') # set title of x-axis
plt.ylabel ('Number of irises') # set title of y-axis
plt.subplots_adjust (top=.9) # adjust the size of the graph to prevent title being cut off
plt.savefig ('C:\\Users\\amand\\Desktop\\GMIT\\Programming\\pands-project2021\\petal_length.png') # save the figure generated
plt.show() # show the figure generated

# petalwidth.py
# This program plots a histogram with petal width in cm on the x-axis and the amount of irises on the y-axis. 
# Using Seaborn's "hue" parameter, we pass the Iris species (class) as a third variable and save the resulting graph as a .png.
# Author: Amanda Murray

import matplotlib.pyplot as plt # a low level graph plotting library in Python
import pandas as pd # a Python library used for working with datasets
import seaborn as sns # A library that uses matplotlib underneath to plot graphs

data = pd.read_csv('C:\\Users\\amand\\Desktop\\GMIT\\Programming\\pands-project2021\\iris.csv') # importing the .csv file
sns.set_style("whitegrid")
sns.FacetGrid(data, hue = 'class', height = 5).map(sns.histplot, 'petal_width', bins = 5).add_legend(title = 'Species')
# Using the Facet Grid, we can assign petal width to the x-axis and the amount of irises on the y-axis.
# Using the 'hue' parameter, we can assign a third variable (class) in different colours.
# height refers to the height in inches of the grid
# Using sns.histplot to generate the histogram
# Using bins to pool the data
# Adding a legend for the colours
plt.title ('Petal widths of the iris species in the Iris data set') # set the title
plt.xlabel ('Petal width (cm)') # set title of x-axis
plt.ylabel ('Number of irises') # set title of y-axis
plt.subplots_adjust (top=.9) # adjust the size of the graph to prevent title being cut off
plt.savefig ('C:\\Users\\amand\\Desktop\\GMIT\\Programming\\pands-project2021\\petal_width.png') # save the figure generated
plt.show() # show the figure generated

# sepallength.py
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

# sepalwidth.py
# This program plots a histogram with sepal width in cm on the x-axis and the amount of irises on the y-axis. 
# Using Seaborn's "hue" parameter, we pass the Iris species (class) as a third variable and save the resulting graph as a .png.
# Author: Amanda Murray

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

# scatterpetals.py
# This program plots a scatter plot with the petal length in cm on the x-axis and petal width in cm on the y-axis. 
# Using Seaborn's "hue" parameter, we pass the Iris species (class) as a third variable and save the resulting graph as a .png.
# Author: Amanda Murray

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = pd.read_csv('C:\\Users\\amand\\Desktop\\GMIT\\Programming\\pands-project2021\\iris.csv')
sns.set_style("white") # instead of using a grid, this program uses a blank white background for the scatterpoints
sns.FacetGrid(data, hue = 'class', height = 5).map(sns.scatterplot, 'petal_length', 'petal_width', s = 100).add_legend(title = 'Species')
# Notice we are calling two variables here rather than one variable for the histogram
# We use the sns.scatterplot function instead of the sns.histplot function
# We specify the size of the scatterpoints instead of selecting a number of bins to pool the data into
plt.title ('Petal lengths and widths of the iris species in the Iris data set')
plt.xlabel ('Petal length (cm)')
plt.ylabel ('Petal width (cm)')
plt.subplots_adjust (top=.9)
plt.savefig ('C:\\Users\\amand\\Desktop\\GMIT\\Programming\\pands-project2021\\scatter_petals.png')
plt.show()

# scattersepals.py
# This program plots a scatter plot with the sepal length in cm on the x-axis and sepal width in cm on the y-axis. 
# Using Seaborn's "hue" parameter, we pass the Iris species (class) as a third variable and save the resulting graph as a .png.
# Author: Amanda Murray

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
# Author: Amanda Murray

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
# Author: Amanda Murray

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