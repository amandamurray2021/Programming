import pandas as pd 

filename = 'C:\\Users\\amand\\Desktop\\GMIT\\Programming\\pands-project2021\\iris.data'
workbookfilename = 'C:\\Users\\amand\\Desktop\\GMIT\\Programming\\pands-project2021\\iris.csv'
df = pd.read_csv(filename, names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])
df.to_csv(workbookfilename, index = False)
print (df)