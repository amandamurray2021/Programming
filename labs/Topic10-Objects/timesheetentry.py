# Q1
# In a file called timesheetentry.py, create a class called Timesheetentry that has three
# attributes that are all set by an __init__ function
# a. Project
# b. Starttime (a date/time object)
# c. Duration (in minutes)
# Author: Amanda Murray

import datetime as dt

class Timesheetentry:

    def __init__(self, project, start, duration):
        self.project = project
        self.start = start
        self.duration = duration

# Q2
# Write a __str__ function for this class that returns the project and the duration

    def __str__(self):
        return self.project + ':' + str(self.duration)

# Q3
# Write a test case for this class that creates an instance and prints it out

if __name__ == '__main__':
    ts = dt.datetime (2021,3,19,16,20)
    test = Timesheetentry ('test', ts, 60)
    print (test)