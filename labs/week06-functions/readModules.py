# Q5
# This program reads in the modules until the user enters a blank for the module name.
# Author: Amanda Murray

def readModules ():
    modules = []
    moduleName = input ("\t Enter the first module name (blank to quit):").strip()

    while moduleName != "":
        module = {}
        module ["name"] = moduleName
        module ["grade"] = int(input("\t\t Enter grade:"))
        modules.append(module)
        moduleName = input("\t Enter next module name (blank to quit):").strip()

    return modules

def doAdd (students):
    currentStudent = {}
    currentStudent ["name"] = input ("Enter name: ")
    currentStudent ["modules"] = readModules ()
    
    students.append (currentStudent)

#test
students = []
doAdd (students)
doAdd (students)
print (students)