import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = pd.read_csv('C:\\Users\\amand\\Desktop\\GMIT\\Programming\\pands-project2021\\iris.csv')
sns.set_style("white")
sns.FacetGrid(data, hue = 'class', height = 5).map(sns.scatterplot, 'sepal_length', 'sepal_width', s = 100).add_legend(title = 'Species')
plt.title ('Sepal lengths and widths of the iris species in the Iris dataset')
plt.xlabel ('Sepal length (cm)')
plt.ylabel ('Sepal width (cm)')
plt.subplots_adjust (top=.9)
plt.savefig ('C:\\Users\\amand\\Desktop\\GMIT\\Programming\\pands-project2021\\scatter_sepals.png')
plt.show()