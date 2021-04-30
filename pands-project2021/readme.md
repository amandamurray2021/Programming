# Project
This project concerns the well-known Fisher’s Iris data set. You must research the data set and write documentation and code (in Python) to investigate it.

## Objectives
1. Research the data set online and write a summary about it in your README. 
2. Download the data set and add it to your repository. 
3. Write a program called analysis.py that:  
• outputs a summary of each variable to a single text file,   
• saves a histogram of each variable to png files, and   
• outputs a scatter plot of each pair of variables. 

Please note that although all of the code will be housed in analysis.py at the end of this project, this README is going to analyse the results of each file that was
created in order to research the data.

## Table of Contents
* analysis.py
* class.png
* class.py
* input.py
* iris.csv
* iris.data
* petal_length.png
* petal_width.png
* petallength.py
* petalwidth.py
* scatter_length.png
* scatter_petals.png
* scatter_sepals.png
* scatter_width.png
* scatterlength.py
* scatterpetals.py
* scattersepals.py
* scatterwidth.py
* sepal_length.png
* sepal_width.png
* sepallength.py
* sepalwidth.py
* summary.py
* summaryofvariables.txt

## Getting Started
First, we need to download the Iris data set. I have chosen to download it from the [UCI Machine Learning Repository.](https://archive.ics.uci.edu/ml/datasets/iris) 

Next, we need to determine what Python libraries we need to analyse this data. As I've written this code in VS Code running Anaconda, I can import them instead of
installing each of them individually.

This project uses the following libraries (using their abbreviations to call them):

`import matplotlib.pyplot as plt`

*Matplotlib is a low level graph plotting library in python that serves as a visualization utility (w3schools).*

`import pandas as pd`

*Pandas is a Python library used for working with data sets. It has functions for analyzing, cleaning, exploring, and manipulating data (w3schools).*

`import seaborn as sns`

*Seaborn is a library that uses Matplotlib underneath to plot graphs. It will be used to visualize random distributions (w3schools).*

Once you have imported (or installed) the libraries and modules, you're ready to begin analysing the Iris data set!

## summary.py
This program outputs a txt.file (summaryofvariables.txt) which provides a summary of each of the variables we are going to analyse:

> In the Iris data set we have 5 individual variables:
> 1. Petal length in centimetres
> 2. Petal width in centimetres
> 3. Sepal length in centimetres
> 4. Sepal width in centimetres
> 5. Class (the species of iris flowers from the Iris data set)
> 
> Here is a summary of each of the variables we will be reviewing in this project.
> 
> Petal length:
> This is a list of 150 floats measuring the length of petals in centimetres in the following iris species:
> Iris-setosa, Iris-versicolor and Iris-virginica.
> 
> Petal width:
> This is a list of 150 floats measuring the width of petals in centimetres in the following iris species:
> Iris-setosa, Iris-versicolor and Iris-virginica.
> 
> Sepal length:
> This is a list of 150 floats measuring the length of sepals in centimetres in the following iris species:
> Iris-setosa, Iris-versicolor and Iris-virginica.
> 
> Sepal width:
> This is a list of 150 floats measuring the width of sepals in centimetres in the following iris species:
> Iris-setosa, Iris-versicolor and Iris-virginica.
> 
> Class:
> This is a list of 150 names of the Iris species in the data set: Iris-setosa, Iris-versicolor and Iris-virginica.
> There are 50 of Iris-setosa, 50 of Iris-versicolor and 50 of Iris-virginica.
> 
> Using Matplotlib, Pandas and Seaborn:
> * We are going to plot each of these variables in histograms against their class.
> * We are going to plot pairs of variables in scatterplots against their class.

## input.py

The first program we are going to write will import the data set that we have already downloaded (iris.data). As the file is .data, we will need to convert it into
something that can be easily read. In this instance, I have chosen to convert it into a .csv file (iris.csv).

`import pandas as pd`

`filename = 'C:\\Users\\amand\\Desktop\\GMIT\\Programming\\pands-project2021\\iris.data'`  
`workbookfilename = 'C:\\Users\\amand\\Desktop\\GMIT\\Programming\\pands-project2021\\iris.csv'`  
`df = pd.read_csv(filename, names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])`  
`df.to_csv(workbookfilename, index = False)`  
`print (df)`

I have included the file paths to make sure that the file is imported from the correct location and saved in the correct sub-folder in my repository.

Following guidance from [Stack Overflow](https://stackoverflow.com/questions/20845213/how-to-avoid-python-pandas-creating-an-index-in-a-saved-csv), I have removed the
numerical index by using `index = False` as I don't want to have a numerical index which will create a new column and skew the data I'm analysing.

Now that the .csv file of the Iris data set has been created, we can pull the data from it for analysis.

## Analysis of the code used

When I initially set out to plot the Iris data set, I used the Pandas dataframe. Although Panda's does a great job of visualising the data, it has difficulties in joining 4 measurements (petal length, petal width, sepal length, sepal width) which are float64 with class which is an object.

When I found [Geekforgeeks](https://www.geeksforgeeks.org/plotting-graph-for-iris-dataset-using-seaborn-and-matplotlib/) sample code, I noticed that by using Seaborn I could use
less lines of code to achieve the same result.

Using Seaborn, we can map the Iris data set in a grid of rows and columns in relation to how much of the variable appears in the data set. We can also use the `hue = 'class'` parameter to plot a third variable (class) in different colors (Seaborn). This removed the barrier of having to plot class individually.

As a result, I decided to proceed with using Geekforgeek's sample code to inspire me to plot the Iris data set.

### Histogram (e.g. petallength.py)

Let's break down the code used to generate one of the histograms and see what the code does:

`import matplotlib.pyplot as plt`  
`import pandas as pd`  
`import seaborn as sns`

`data = pd.read_csv('C:\\Users\\amand\\Desktop\\GMIT\\Programming\\pands-project2021\\iris.csv')`  
*Using Pandas' [read_csv](https://www.w3schools.com/python/pandas/pandas_csv.asp) function we load our CSV file, making sure to specify the path.*

`sns.set_style("whitegrid")`  
*Using Seaborn's [set_style](https://seaborn.pydata.org/generated/seaborn.set_style.html#seaborn.set_style) function, I am including a grid on the histogram
to allow me to calculate the petal lengths against the amount of irises of each species (class) more accurately.*

`sns.FacetGrid(data, hue = 'class', height = 5).map(sns.histplot, 'petal_length', bins = 5).add_legend(title = 'Species')`  

*Using Seaborn's [Facet Grid](https://seaborn.pydata.org/generated/seaborn.FacetGrid.html#seaborn.FacetGrid), we can assign petal length to the x-axis, the amount of irises
of each species to the y-axis and can also use the `hue = 'class'` parameter to represent our third variable (class) in different colors (Seaborn).*

*`height = 5` refers to the height (in inches) of the grid.*

*Using the [Facet Grid.map](https://seaborn.pydata.org/generated/seaborn.FacetGrid.map.html#seaborn.FacetGrid.map) function allows us to plot the variables we have assigned 
to the Facet Grid.*

*In this instance we are generating a histogram by using the `sns.histplot` function which 'represents the distribution of one or more variables (in this case petal length,
amount of irises, class) by counting the number of observations that fall within disrete bins' (Seaborn).*

*`bins = 5` refers to the number of bins the data will be pooled into, while `add_legend()` simply adds a legend so that we know what each colour is associated with.*

`plt.title ('Petal lengths of the iris species in the Iris data set')`  
`plt.xlabel ('Petal length (cm)')`  
`plt.ylabel ('Number of irises')` 

*These [functions](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.html) allow us to add a title and a label on the X and Y axis.*

`plt.subplots_adjust (top=.9)`

*This [function](https://github.com/mwaskom/seaborn/issues/2072) allows us to adjust the size of the graph. I added this line due to an error with the original
graph cutting off the title.*

`plt.savefig ('C:\\Users\\amand\\Desktop\\GMIT\\Programming\\pands-project2021\\petal_length.png')` 

*This [function](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html) allows us to save the figure that is generated. I have specified the
path again to make sure that the image is going to the right repository. The `petal_length.png` ending serves as the title of the figure being saved.*

`plt.show()`  

*This [function](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html) will show us the figure we have generated.*

The rest of the histograms use identical code, only changing what variables are plotted and the labelling.

### Scatterplot (e.g. scatterpetals.py)

In contrast, let's take a look at the code used to generate one of the scatter plots and jot down the differences:

`import matplotlib.pyplot as plt`  
`import pandas as pd`  
`import seaborn as sns`  

`data = pd.read_csv('C:\\Users\\amand\\Desktop\\GMIT\\Programming\\pands-project2021\\iris.csv')`  
`sns.set_style("white")`  

*Instead of using a grid, this program uses a blank white background. This is more efficient for a scatter plot as we will be looking at scatterpoints rather than
data generated in blocks like a histogram.*
 
`sns.FacetGrid(data, hue = 'class', height = 5).map(sns.scatterplot, 'petal_length', 'petal_width', s = 100).add_legend(title = 'Species')`

*When we are mapping the plot, we use the `sns.scatterplot` function instead of the `sns.histplot` function we used earlier. Additionally, we specify the size of the scatterpoints `s = 100` rather than selecting a number of bins to pool the data into.*

*Notice that we are also calling two variables here, petal length and petal width, instead of the one variable called for the histogram.*

`plt.title ('Petal lengths and widths of the iris species in the Iris data set')`  
`plt.xlabel ('Petal length (cm)')`  
`plt.ylabel ('Petal width (cm)')`  
`plt.subplots_adjust (top=.9)`  
`plt.savefig ('C:\\Users\\amand\\Desktop\\GMIT\\Programming\\pands-project2021\\scatter_petals.png')`  
`plt.show()`

The rest of the code performs the same as the code we used to generate the histogram.

The rest of the scatter plots use identical code, only changing what variables are plotted and the labelling.

## Results

Now that we have determined what the code does, let's look at the results we achieved from the data.

### Histograms

First, let's take a look at the data from the histograms. As the figures cannot be determined with 100% accuracy, please note that a margin of error may exist.

#### petallength.py

* We compared petal length in centimetres (x-axis) against the amount of irises (y-axis). The program also took into account the third variable 'class'. The Iris species
all have different colours which can be matched to the legend on the right.

* Iris-setosa:
Petals are between 1 - 1.9 centimetres in length.

* Iris-versicolor:
Petals are between 3 - 5.1 centimetres in length.

* Iris-virginica:
Petals are between 4.8 - 6.9 centimetres in length.

* While there is a minor overlap (0.3 millimetres) between the length of petals in the Iris-versicolor and the Iris-virginica, the petals on the Iris-setosa are much shorter.

![petallength](https://github.com/amandamurray2021/Programming/blob/main/pands-project2021/petal_length.png)

#### petalwidth.py

* We compared petal width in centimetres (x-axis) against the amount of irises (y-axis). The program also took into account the third variable 'class'. The Iris species
all have different colours which can be matched to the legend on the right.

* Iris-setosa:
Petals are between 0.2 - 0.6 millimetres in width.

* Iris-versicolor:
Petals are between 1 - 1.7 centimetres in width.

* Iris-virginica:
Petals are between 1.4 - 2.5 centimetres in width.

* While there is a minor overlap (0.3 millimetres) between the width of petals in the Iris-versicolor and the Iris-virginica, the petals on the Iris-setosa are much narrower.

![petalwidth](https://github.com/amandamurray2021/Programming/blob/main/pands-project2021/petal_width.png)

#### sepallength.py

* We compared sepal length in centimetres (x-axis) against the amount of irises (y-axis). The program also took into account the third variable 'class'. The Iris species
all have different colours which can be matched to the legend on the right.

* Iris-setosa:
Sepals are between 4.25 - 5.75 centimetres in length.

* Iris-versicolor:
Sepals are between 4.9 - 7 centimetres in length.

* Iris-virginica:
Sepals are between 4.9 - 7.9 centimetres in length.

* This is the first instance where we begin to see an overlap in sizing across all of the Iris species in the Iris data set.

![sepallength](https://github.com/amandamurray2021/Programming/blob/main/pands-project2021/sepal_length.png)

#### sepalwidth.py

* We compared sepal width in centimetres (x-axis) against the amount of irises (y-axis). The program also took into account the third variable 'class'. The Iris species
all have different colours which can be matched to the legend on the right.

* Iris-setosa:
Sepals are between 3.2 - 4.4 centimetres in width.

* Iris-versicolor:
Sepals are between 2 - 3.4 centimetres in width.

* Iris-virginica:
Sepals are between 2.4 - 3.8 centimetres in width.

* Similar to the sepal lengths, there is an overlap in the sepal widths across all of the Iris species in the Iris data set.

![sepalwidth](https://github.com/amandamurray2021/Programming/blob/main/pands-project2021/sepal_width.png)

#### class.py

* We compared the iris species (x-axis) against the amount of irises (y-axis). 

* It shows an equal distribution - 50 of Iris-setosa, 50 of Iris-versicolor and 50 of Iris-virginica.

![class](https://github.com/amandamurray2021/Programming/blob/main/pands-project2021/class.png)

### Scatter plots

Now, let's a look at the data from the scatter plots.

#### scatterpetals.py

* We compared petal length in centimetres (x-axis) against petal width in centimetres (y-axis). The program also took into account the third variable 'class'. The Iris species
all have different colours which can be matched to the legend on the right.

* Similar to the histograms, the scatter plot shows that although there is a minor overlap between the Iris-versicolor and the Iris-virginica's petal length and width, the Iris-setosa's petals are much shorter and narrower than the other species.

![scatterpetals](https://github.com/amandamurray2021/Programming/blob/main/pands-project2021/scatter_petals.png) 

#### scattersepals.py

* We compared sepal length in centimetres (x-axis) against sepal width in centimetres (y-axis). The program also took into account the third variable 'class'. The Iris species
all have different colours which can be matched to the legend on the right.

* The histograms (sepallength.py, sepalwidth.py) suggest an overlap of sepal length and width across all of the Iris species.

* The scatter plot suggests that while there is considerable overlap between the Iris-versicolor and the Iris-virginica, the Iris-setosa's sepals are shorter and wider so they don't overlap with their counterparts at all.

* Interestingly, we find 1 Iris-setosa listed as 2.3 centimetres in width. This was missed in the histogram (due to the stacked effect) but is much easier to pinpoint as
part of the scatter plot.

![scattersepals](https://github.com/amandamurray2021/Programming/blob/main/pands-project2021/scatter_sepals.png)

#### scatterlength.py

* We compared petal length in centimetres (x-axis) against sepal length in centimetres (y-axis). The program also took into account the third variable 'class'. The Iris species
all have different colours which can be matched to the legend on the right.

* Although the histograms (petallength.py, sepallength.py) confirm that there is no correlation between Iris-setosa, Iris-versicolor and Iris-virginica in petal length, they
suggest an overlap of sepal length across all of the Iris species.

* The scatter plot suggests that while there is considerable overlap between the Iris-versicolor and the Iris-virginica's sepal lengths, the Iris-setosa's sepals are far shorter and don't overlap with their counterparts at all.

![scatterlength](https://github.com/amandamurray2021/Programming/blob/main/pands-project2021/scatter_length.png)

#### scatterwidth.py

* We compared petal width in centimetres (x-axis) against sepal width in centimetres (y-axis). The program also took into account the third variable 'class'. The Iris species
all have different colours which can be matched to the legend on the right.

* Although the histograms (petalwidth.py, sepalwidth.py) confirm that there is no correlation between Iris-setosa, Iris-versicolor and Iris-virginica in petal width, they
suggest an overlap of sepal width across all of the Iris species.

* The scatter plot suggests that while there is an overlap between the Iris-versicolor and the Iris-virginica's sepal width, the Iris-setosa's sepals are wider and don't overlap with their counterparts at all.

![scatterwidth](https://github.com/amandamurray2021/Programming/blob/main/pands-project2021/scatter_width.png)

### Conclusion

Interestingly, the data that was plotted in the histograms didn't correlate with the data that was plotted in the scatterplots. This suggests that a method of using multiple
visualisations of data is prudent in order to improve the accuracy of your results.

## Works Cited
Anderson, Edgar. “The Species Problem in Iris.” Annals of the Missouri Botanical Garden, vol. 23, no. 3, 1936, pp. 457–509. JSTOR, www.jstor.org/stable/2394164.  

Bhalla, Deepanshu. “How to Import Data in Python.” ListenData, RSGB Business Consultant Pvt. Ltd, www.listendata.com/2017/02/import-data-in-python.html#Import-CSV-files. Accessed 23 Apr. 2021.  

“Change Axis Labels, Set Title and Figure Size to Plots with Seaborn.” Data Viz with Python and R, datavizpyr.com/change-axis-labels-set-title-and-figure-size-to-plots-with-seaborn. Accessed 25 Apr. 2021.  

Cone, Matt. “Basic Syntax | Markdown Guide.” Markdownguide, www.markdownguide.org/basic-syntax. Accessed 30 Apr. 2021.  

“Csv — CSV File Reading and Writing — Python 3.9.4 Documentation.” Python, Python Software Foundation, docs.python.org/3/library/csv.html. Accessed 25 Apr. 2021.  

Fisher, R. A. “The Use of Multiple Measurements in Taxonomic Problems.” Annals of Eugenics, vol. 7, no. 2, 1936, pp. 179–88. Wiley Online Library, onlinelibrary.wiley.com/doi/abs/10.1111/j.1469-1809.1936.tb02137.x.  

GeeksforGeeks. “Plotting Graph For IRIS Dataset Using Seaborn And Matplotlib.” GeeksforGeeks, 4 Mar. 2021, www.geeksforgeeks.org/plotting-graph-for-iris-dataset-using-seaborn-and-matplotlib.  

“How to Avoid Python/Pandas Creating an Index in a Saved Csv?” Stack Overflow, Stack Exchange Inc, stackoverflow.com/questions/20845213/how-to-avoid-python-pandas-creating-an-index-in-a-saved-csv. Accessed 26 Apr. 2021.  

Hunter, John, et al. “Matplotlib.Pyplot — Matplotlib 3.4.1 Documentation.” Matplotlib, matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.html. Accessed 30 Apr. 2021.  

---. “Matplotlib.Pyplot.Savefig — Matplotlib 3.4.1 Documentation.” Matplotlib, matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html. Accessed 30 Apr. 2021.  

---. “Matplotlib.Pyplot.Show — Matplotlib 3.4.1 Documentation.” Matplotlib, matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html. Accessed 30 Apr. 2021.  

---. “Matplotlib.Pyplot.Subplots_adjust — Matplotlib 3.1.2 Documentation.” Matplotlib, matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.subplots_adjust.html. Accessed 30 Apr. 2021.  

“Iris.Py.” Bokeh, NumFOCUS, docs.bokeh.org/en/latest/docs/gallery/iris.html. Accessed 25 Apr. 2021.  

Kozak, Marcin, and Barbara Lotocka. “What Should We Know about the Famous Iris Data?” Current Science, vol. 104, no. 5, 2013, pp. 579–80. JSTOR, www.jstor.org/stable/24089851.  

“Matplotlib Labels and Title.” W3Schools, Refsnes Data, www.w3schools.com/python/matplotlib_labels.asp. Accessed 20 Apr. 2021.  

“Matplotlib Legend.” Pythonspot, 28 July 2016, pythonspot.com/matplotlib-legend. Accessed 20 Apr. 2021.  

“Matplotlib Tutorial.” W3Schools, Refsnes Data, www.w3schools.com/python/matplotlib_intro.asp. Accessed 30 Apr. 2021.  

McCullum, Nick. “How To Create Scatterplots in Python Using Matplotlib.” Nickmccullum, nickmccullum.com/python-visualization/scatterplot. Accessed 25 Apr. 2021.  

Narula, Manav. “Convert Object to Float in Pandas.” Delft Stack, 23 Dec. 2020, www.delftstack.com/howto/python-pandas/pandas-convert-object-to-float.  

“Pandas - Analyzing DataFrames.” W3Schools, Refsnes Data, www.w3schools.com/python/pandas/pandas_analyzing.asp. Accessed 24 Apr. 2021.  

“Pandas - Plotting.” W3Schools, Refsnes Data, www.w3schools.com/python/pandas/pandas_plotting.asp. Accessed 24 Apr. 2021.  

“Pandas DataFrames.” W3Schools, Refsnes Data, www.w3schools.com/python/pandas/pandas_dataframes.asp. Accessed 24 Apr. 2021.  

“Pandas Introduction.” W3Schools, Refsnes Data, www.w3schools.com/python/pandas/pandas_intro.asp. Accessed 30 Apr. 2021.  

“Pandas Read CSV.” W3Schools, Refsnes Data, www.w3schools.com/python/pandas/pandas_csv.asp. Accessed 23 Apr. 2021.  

“Pandas Scatter Plot - DataFrame.Plot.Scatter().” Data Independent, 10 Aug. 2020, www.dataindependent.com/pandas/pandas-scatter-plot.  

“Pandas.DataFrame.Plot — Pandas 1.2.4 Documentation.” Pandas, pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.html. Accessed 23 Apr. 2021.  

“Pandas.DataFrame.Plot.Hist — Pandas 1.2.4 Documentation.” Pandas, pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.hist.html. Accessed 23 Apr. 2021.  

“Pandas.DataFrame.Plot.Scatter — Pandas 1.2.4 Documentation.” Pandas, pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.scatter.html. Accessed 25 Apr. 2021.  

“Pandas.DataFrame.To_csv — Pandas 1.2.4 Documentation.” Pandas, pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html. Accessed 25 Apr. 2021.  

“Python Machine Learning Scatter Plot.” W3Schools, Refsnes Data, www.w3schools.com/python/python_ml_scatterplot.asp. Accessed 23 Apr. 2021.  

Sambhu. “Exploratory Data Analysis: Iris DataSet - Analytics Vidhya.” Medium, 4 Apr. 2020, medium.com/analytics-vidhya/exploratory-data-analysis-iris-dataset-32d09a52f322.  

“Seaborn.” W3Schools, Refsnes Data, www.w3schools.com/python/numpy/numpy_random_seaborn.asp. Accessed 30 Apr. 2021.  

UCI Donald Bren School of Information & Computer Sciences. “UCI Machine Learning Repository: Iris Data Set.” UCI Machine Learning Repository - Center for Machine Learning and Intelligent Systems, archive.ics.uci.edu/ml/datasets/iris. Accessed 20 Apr. 2021.  

VanderPlas, Jake. Python Data Science Handbook. 1st ed., Sebastopol, CA, O’ Reilly Media, 2016. O’ Reilly Online Learning, www.oreilly.com/library/view/python-data-science/9781491912126/ch04.html.  

“Visualization — Pandas 1.2.4 Documentation.” Pandas, pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html. Accessed 26 Apr. 2021.  

Waskom, Michael. “API Reference — Seaborn 0.11.1 Documentation.” Seaborn, seaborn.pydata.org/api.html. Accessed 25 Apr. 2021.  

---. “Seaborn.FacetGrid — Seaborn 0.11.1 Documentation.” Seaborn, seaborn.pydata.org/generated/seaborn.FacetGrid.html#seaborn.FacetGrid. Accessed 25 Apr. 2021.  

---. “Seaborn.FacetGrid.Map — Seaborn 0.11.1 Documentation.” Seaborn, seaborn.pydata.org/generated/seaborn.FacetGrid.map.html#seaborn.FacetGrid.map. Accessed 25 Apr. 2021.  

---. “Seaborn.Histplot — Seaborn 0.11.1 Documentation.” Seaborn, seaborn.pydata.org/generated/seaborn.histplot.html. Accessed 28 Apr. 2021.  

---. “Seaborn.Scatterplot — Seaborn 0.11.1 Documentation.” Seaborn, seaborn.pydata.org/generated/seaborn.scatterplot.html. Accessed 28 Apr. 2021.  

---. “Seaborn.Set_style — Seaborn 0.11.1 Documentation.” Seaborn, seaborn.pydata.org/generated/seaborn.set_style.html#seaborn.set_style. Accessed 25 Apr. 2021.  

---. “Top Half of Seaborn Chart Title Gets Cut Off · Issue #2072 · Mwaskom/Seaborn.” GitHub, 14 May 2020, github.com/mwaskom/seaborn/issues/2072.  
