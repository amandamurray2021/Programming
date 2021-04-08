# Q4
# Write a class called Employee (in employee.py) that has one attribute called timesheets
# (set as an empty list) and an __init__ function that takes in a first and last name
# Author: Amanda Murray

import datetime as dt
from timesheetentry import *

class Employee:
    timesheets = []

    def __init__ (self, first, last):
        self.first = first
        self.last = last
# Q5
# Write a __str__ function that returns the full name
    def __str__ (self):
        return self.first + ' ' + self.last

# Q6
# Write a testcase (see Q9)

# if __name__ == "__main__":
#    test = Employee ('some', 'one')
#    print (test)
#    assert ( 'some one' == str(test))

# Q7
# Write a function in the class Employee called logminutes (project, minutes).
# The function will create a Timesheetentry with the project and minutes and
# the time being now (it should probably be now minus minutes) and append it
# to the list

    def logminutes (self, project, minutes):
        now = dt.datetime.now
        timesheetentry = Timesheetentry (project, now, minutes)
        self.timesheets.append (timesheetentry)

# Q8
# Write a function called gettotaltime() that will return the total minutes
# of all the timesheetentries

    def gettotaltime(self):
        total_minutes = 0
        for ts in self.timesheets:
            total_minutes += ts.duration
            return total_minutes

# Q9
# Write a test case for this

if __name__ == '__main__':
    test = Employee ('some', 'one')
    print (test)
    assert( 'some one' == str(test))
    test.logminutes ('pl', 30)
    test.logminutes ('pl', 60)
    mins = test.gettotaltime()
    assert (mins == 90)
    print (mins)
    print ('all good')