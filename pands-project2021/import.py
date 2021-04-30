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