# Q11
# Write a program that has a list of counties, making sure it is a long list (5 counties)
# Make some counties appear more than others.
# Make a pie chart of the counties.
# Author: Amanda Murray

import numpy as np
import matplotlib.pyplot as plt 

# make the array of occurrences
possibleCounties = ["Galway", "Cork", "Kerry", "Kilkenny", "Tipperary"]

# pick 100 randomly from possible counties with the frequence set in p
counties = np.random.choice (
    possibleCounties , 
    p = [0.1, 0.3, 0.2, 0.12, 0.28],
    size = (100)
)

# right now we need the number of occurrences of each county
# this returns a tuple of the unique values and how many times they appear
unique, counts = np.unique(counties, return_counts = True)

# we can now put this into a pie plot
plt.pie (counts, labels = unique)
plt.show()