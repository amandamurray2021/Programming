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