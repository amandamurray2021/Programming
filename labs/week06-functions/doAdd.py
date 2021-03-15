# This program reads in the student's name, module names and grades
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