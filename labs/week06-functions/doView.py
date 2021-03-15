# This program prints out all of the student's names first
# Then it runs a function called displayModules() and calls it afterwards to print each name
# Author: Amanda Murray

def displayModules(modules):
    print ("\t Name \t Grade")
    for module in modules:
        print ("\t{} \t{}".format (module ["name"], module ["grade"]))

def doView (students):
    for currentStudent in students:
        print (currentStudent["name"])
        displayModules (currentStudent ["modules"])