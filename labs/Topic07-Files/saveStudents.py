# Q6
# Put the savedict() function into the program and call it from the dosave() function.
# Author: Amanda Murray

import json
# the array we store everything in
students = []
filename = "students.json"
def writeDict(obj):
    with open(filename, 'wt') as f:
        json.dump(obj, f)

def displayMenu ():
    print ("What would you like to do?")
    print ("\t (a) Add new student")
    print ("\t (v) View students")
    print ("\t (s) Save students")
    print ("\t (q) Quit")
    choice = input ("Type one letter (a/v/s/q):").strip()
    
    return choice

def doAdd (students):
    currentStudent = {}
    currentStudent ["name"] = input ("Enter name: ")
    currentStudent ["modules"] = readModules ()
    students.append (currentStudent)

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

def displayModules(modules):
    print ("\tName \tGrade")
    for module in modules:
        print ("\t{} \t{}".format(module["name"], module["grade"]))

def doView (students):
    for currentStudent in students:
        print (currentStudent["name"])
        displayModules(currentStudent ["modules"])

def doSave (students):
    writeDict(students)
    print ("students saved")

# main program
choice = displayMenu ()
while (choice != 'q'):
    # we could do this with lamda functions
    # I am keeping this basic for the moment
    if choice == 'a':
        doAdd(students)
    elif choice == 'v':
        doView (students)
    elif choice == 's':
        doSave(students)
    elif choice != 'q':
        print ("\n\n please select either a, v, s or q")
    choice = displayMenu ()