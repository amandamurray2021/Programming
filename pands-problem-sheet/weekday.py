# Weekly Task 5
# This program outputs whether or not today is a weekday
# Author: Amanda Murray

import datetime #I need to import Python's datetime module so it can tell me if it's a weekday or the weekend
print (input ("Please enter a weekday: "))

day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
daysoftheweek = day [datetime.date.weekday()]
#weekday = (day [0:4])
#weekend = (day [5:7])

for input in day(daysoftheweek(range (0,5))):
    print ("Yes, unfortunately today is a weekday")

for input in day(daysoftheweek(range (6,8))):
    print ("It is the weekend, yay!")