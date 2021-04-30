import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = pd.read_csv('C:\\Users\\amand\\Desktop\\GMIT\\Programming\\pands-project2021\\iris.csv')
sns.set_style("white")
sns.FacetGrid(data, hue = 'class', height = 5).map(sns.scatterplot, 'petal_length', 'petal_width', s = 100).add_legend(title = 'Species')
plt.title ('Petal lengths and widths of the iris species in the Iris dataset')
plt.xlabel ('Petal length (cm)')
plt.ylabel ('Petal width (cm)')
plt.subplots_adjust (top=.9)
plt.savefig ('C:\\Users\\amand\\Desktop\\GMIT\\Programming\\pands-project2021\\scatter_petals.png')
plt.show()