# Q2
# This program allows a user to create new students and to view students.
# It is a function that prints out a menu of commands we can perform (ie add, view and quit).
# The program returns what the user chose.
# Author: Amanda Murray

def displayMenu ():
    print ("What would you like to do?")
    print ("\t (a) Add new student")
    print ("\t (v) View students")
    print ("\t (q) Quit")
    choice = input ("Type one letter (a/v/q):").strip ()

    return choice

choice = displayMenu ()
print ("You chose {}".format (choice))