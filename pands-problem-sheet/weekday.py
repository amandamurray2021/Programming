# Weekly Task 5
# This program outputs whether or not today is a weekday
# Author: Amanda Murray

import datetime #I need to import Python's datetime module so it can tell me if it's a weekday or the weekend
print (input ("Please enter a weekday: "))

day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"] 
daysoftheweek = day [datetime.date.weekday()]
#weekday = (day [0:4]) # Here I tried to use list slicing to pull the first 5 values as the weekday
#weekend = (day [5:7]) # Here I tried to use list slicing to pull the final 2 values as the weekend

for input in day(daysoftheweek(range (0,5))): # Here I tried to pull the input from the top line and have it determine that if the 
    print ("Yes, unfortunately today is a weekday") # range is between 0 and 5 it is a weekday

for input in day(daysoftheweek(range (6,8))): # Here I tried to pull the input from the top line and have it determine that if the
    print ("It is the weekend, yay!") # range is between 6 and 8 it is the weekend

# Although this code is not functioning at the moment, I realised last minute that I should have been using 
# datetime.date.today() and the datetime.weekday() functions to pull today's date and from that it would be possible
# to determine if it's a weekday or the weekend