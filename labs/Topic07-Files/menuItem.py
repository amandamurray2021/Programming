# Q5
# This program creates a new menu item called save.
# When the user selects it the doSave() function should be called.
# Author: Amanda Murray

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

def doView (students):
    for currentStudent in students:
        print (currentStudent["name"])
        displayModules(currentStudent ["modules"])

def doSave (students):
    # You will put the call to save dict here
    print ("in save")

students = []
choice = displayMenu ()
while (choice != 'q'):
    if choice == 'a':
        doAdd (students)
    elif choice == 'v':
        doView (students)
    elif choice == 's':
        doSave (students)
    elif choice != 'q':
        print ("\n\n please select either a, v, s or q")
    choice = displayMenu ()