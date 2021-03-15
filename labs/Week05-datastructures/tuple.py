# This program stores the months of the year in a tuple
# From this tuple, we need to create another tuple with the summer months May, June, July
# We also need to have the program print out the summer months one at a time
# Author: Amanda Murray

months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
summer = months[4:7]
for month in summer:
    print (month)