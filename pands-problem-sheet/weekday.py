# Weekly Task 5
# This program outputs whether or not today is a weekday
# Author: Amanda Murray

import datetime # I need to import Python's datetime module to handle dates/times/days in Python

x = datetime.date.today().weekday()
# datetime.date.today() returns the current local date
# datetime.date.weekday() returns the day of the week as an integer, where Monday is 0 and Sunday is 6
# days of the week: Monday = 0, Tuesday = 1, Wednesday = 2, Thursday = 3, Friday = 4, Saturday = 5, Sunday = 6

if x <= 4: # Using less than or equal to 4 will cover the days of the week from Monday to Friday (0 - 4)
    print ("Yes, unfortunately today is a weekday")
else:
    x > 4 # Once the integer expressing the days of the week is greater than 4 (ie. 5 or 6) it is the weekend
    print ("It is the weekend, yay!")

# Concept for this code influenced by Stack Overflow's sample code (see Works Cited)