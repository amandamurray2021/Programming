# Q4
# We are now going to write the function doAdd(students).
# This program reads in the student's name, module names and grades.
# It creates a student dict we can print out.
# We should add the student dict to list (pass this list in).
# Author: Amanda Murray

students = []
def readModules ():
    return []

def doAdd (students):
    currentStudent = {}
    currentStudent ["name"] = input ("Enter name: ")
    currentStudent ["modules"] = readModules ()
    
    students.append (currentStudent)

doAdd (students)
print (students)