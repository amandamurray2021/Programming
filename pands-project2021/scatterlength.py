import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = pd.read_csv('C:\\Users\\amand\\Desktop\\GMIT\\Programming\\pands-project2021\\iris.csv')
sns.set_style("white")
sns.FacetGrid(data, hue = 'class', height = 7).map(plt.scatter, 'petal_length', 'sepal_length', s = 100).add_legend(title = 'Species')
plt.title ('Petal and sepal lengths of the iris species in the Iris dataset')
plt.xlabel ('Petal length (cm)')
plt.ylabel ('Sepal length (cm)')
plt.show()